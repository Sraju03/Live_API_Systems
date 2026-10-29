
import requests

from epita_raju_sekar_space.config import config


NASA_APOD_URL = (
    "https://science.nasa.gov/wp-json/wp/v2/apod-basic/"
)


def fetch_live_data(date: str | None = None) -> dict:
    """Fetch live APOD data from NASA."""

    config.validate()

    params = {
        "api_key": config.api_key,
    }

    if date:
        params["date"] = date

    try:
        response = requests.get(
            NASA_APOD_URL,
            params=params,
            timeout=(5, 30),
        )

        response.raise_for_status()

        data = response.json()

        # NASA's updated endpoint returns a list.
        if isinstance(data, list):
            if not data:
                raise RuntimeError(
                    "NASA API returned an empty list."
                )

            # Select the first APOD record.
            data = data[0]

        # Verify that the result is a dictionary.
        if not isinstance(data, dict):
            raise RuntimeError(
                "Unexpected NASA API response format."
            )

        return {
            "status": "LIVE_SUCCESS",
            "date": data.get("date"),
            "title": data.get("title"),
            "media_type": data.get("media_type"),
            "explanation": data.get("explanation"),
            "url": data.get("url") or data.get("permalink"),
            "copyright": data.get("copyright"),
        }

    except requests.exceptions.Timeout as exc:
        raise RuntimeError(
            "NASA API request timed out."
        ) from exc

    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(
            f"NASA API returned HTTP "
            f"{exc.response.status_code}"
        ) from exc

    except requests.exceptions.RequestException as exc:
        raise RuntimeError(
            "Unable to connect to NASA API."
        ) from exc
