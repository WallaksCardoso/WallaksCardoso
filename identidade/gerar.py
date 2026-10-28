import os
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlencode

BASE = Path(__file__).parent
SAIDA = BASE.parent / "img"
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

BANNER = {
    "repo": "github.com/WallaksCardoso",
    "titulo": "Wallaks Cardoso",
    "descricao": "Desenvolvedor back-end em Java, Spring Boot e Kafka.",
    "stack": "Java,Spring Boot,Kafka,PostgreSQL,Docker",
    "icone": "code-xml",
}

PROJETOS = [
    ("painel-financeiro", "Painel Financeiro",
     "Fluxo de caixa pessoal: faturas, parcelas, recorrências e dívidas.",
     "Python,FastAPI,React,TypeScript,Docker", "chart-line", "Full stack"),
    ("pelada-gestao", "Pelada Gestão",
     "API em microsserviços para organizar a pelada e sortear os times.",
     "Java 21,Spring Boot,Kafka,PostgreSQL,Docker", "trophy", "Back-end"),
    ("spring-jwt-auth", "Spring JWT Auth",
     "Autenticação stateless com JWT para os serviços da pelada.",
     "Java 21,Spring Security,JWT,PostgreSQL", "shield-check", "Back-end"),
    ("email-service", "Email Service",
     "Notificações por e-mail a partir de eventos do Kafka, com novas tentativas.",
     "Java 21,Spring Boot,Kafka,Docker", "mail", "Back-end"),
    ("sorteio-times", "Sorteio de Times",
     "PWA para sortear os times no celular e mandar no WhatsApp.",
     "TypeScript,Vite,PWA,Vitest", "shuffle", "Front-end"),
    ("pelada-gestao-front-web", "Panelinha",
     "Interface em Flutter: listas, jogadores e sorteio dos times.",
     "Flutter,Dart,Docker", "smartphone", "Front-end"),
    ("algoritmo-genetico-java", "Algoritmo Genético",
     "Otimização da carga de um caminhão baú com o problema da mochila.",
     "Java,Maven,JUnit", "dna", "Algoritmos"),
    ("ambiente-dev", "Ambiente Dev",
     "Documentação do ambiente escrita no Notion e publicada no GitHub Pages.",
     "GitHub Actions,Jekyll,Notion API", "terminal", "Documentação"),
]


def capturar(modelo, parametros, destino, largura, altura):
    url = (BASE / modelo).as_uri() + "?" + urlencode(parametros)
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        f"--window-size={largura},{altura}", "--virtual-time-budget=8000",
        f"--screenshot={destino}", url,
    ], check=True, capture_output=True)
    print(destino.name)


def gerar_capa(repo, titulo, descricao, stack, icone, categoria):
    parametros = {
        "repo": repo, "titulo": titulo, "descricao": descricao,
        "stack": stack, "icone": icone, "categoria": categoria,
    }
    capturar("capa.html", parametros, SAIDA / f"{repo}.png", 1280, 640)


def gerar_banner():
    capturar("banner.html", BANNER, SAIDA / "banner.png", 1280, 360)


if __name__ == "__main__":
    SAIDA.mkdir(exist_ok=True)
    pedidos = sys.argv[1:]
    if not pedidos or "banner" in pedidos:
        gerar_banner()
    for projeto in PROJETOS:
        if not pedidos or projeto[0] in pedidos:
            gerar_capa(*projeto)
