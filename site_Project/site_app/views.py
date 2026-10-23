
import json
import os

from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import URLError

from django.shortcuts import render


def catalogo(request):
    termo = request.GET.get("q", "Batman").strip()

    filmes = []
    erro = None

    chave = os.environ.get("OMDB_API_KEY")

    if not chave:
        erro = "Chave da API não configurada."

    elif termo:
        parametros = urlencode({
            "apikey": chave,
            "s": termo,
            "type": "movie"
        })

        url = "https://www.omdbapi.com/?" + parametros

        try:
            with urlopen(url, timeout=10) as resposta:
                dados = json.load(resposta)

            if dados.get("Response") == "True":
                filmes = dados.get("Search", [])
            else:
                erro = "Nenhum filme encontrado."

        except (URLError, TimeoutError, ValueError):
            erro = "Erro ao consultar a API."

    return render(request, "tela.html", {
        "filmes": filmes,
        "termo": termo,
        "erro": erro
    })

