"""A simple API to expose our trained RandomForest model for Tutanic survival."""

import io
from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
import polars as pl

app = FastAPI(
    title="UMAP API",
    description="Application de réduction de dimension avec l'algorithme UMAP"
)


@app.get("/", tags=["Welcome"])
def show_welcome_page():
    """
    Show welcome page with model name and version.
    """

    return {
        "Message": "UMAP API",
        "Model_name": "UMAP",
        "Model_version": "0.1",
    }


@app.get("/predict", tags=["umap"]) # keep for testing the api
async def predict(
    sex: str = "female", age: float = 29.0, fare: float = 16.5, embarked: str = "S"
) -> str:
    """ """

    df = pd.DataFrame(
        {
            "Sex": [sex],
            "Age": [age],
            "Fare": [fare],
            "Embarked": [embarked],
        }
    )

    prediction = "Survived 🎉" 

    return prediction

@app.post(
    "/umap",
    summary="Return the first 5 rows of an uploaded CSV file",
    response_description="A list of the first 5 rows, each row represented as a dict",
)
async def umap(file: UploadFile = File(...)) -> str:
    """
    Accept a CSV file via multipart/form‑data and return the first five rows.

    Parameters
    ----------
    file : UploadFile
        The CSV file uploaded by the client.

    Returns
    -------
    JSONResponse
        JSON object with a single key ``preview`` containing a list of
        row dictionaries.

    Raises
    ------
    HTTPException
        * 400 – if the file is not a CSV or cannot be parsed.
    """
    # Basic file‑type check
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are accepted. "
            f"Received: {file.filename}",
        )

    try:
        # Read the entire file into memory – suitable for small‑to‑medium CSVs.
        # For huge files consider a streaming/partial read approach.
        content = await file.read()
        buffer = io.BytesIO(content)

        # Polars can read from a file‑like object.
        df = pl.read_csv(buffer)

        # Grab the first five rows.
        repr_str = df.head(5).__repr__()     # or df.__str__()

    except Exception as exc: 
        # Polars raises a variety of exceptions on malformed data.
        raise HTTPException(
            status_code=400,
            detail=f"Could not parse CSV file: {exc}",
        ) from exc

    return repr_str #JSONResponse(content={"preview": preview})
