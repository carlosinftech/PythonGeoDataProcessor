import pandas as pd
import requests

url = "https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-152027/valeursfoncieres-2022-s1.txt"


urls = ["https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-152027/valeursfoncieres-2022-s1.txt",
        "https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-151704/valeursfoncieres-2021.txt",
        "https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-151136/valeursfoncieres-2020.txt",
        "https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-150616/valeursfoncieres-2019.txt",
        "https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-145753/valeursfoncieres-2018.txt",
        "https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-145353/valeursfoncieres-2017-s2.txt"]
# Make an API request to retrieve the data
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open("output.txt", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

else:
    # If the request was unsuccessful, raise an error
    raise Exception("Request to API failed with status code {}".format(response.status_code))
