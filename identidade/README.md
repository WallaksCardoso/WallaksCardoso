# Identidade visual

Gera o banner do perfil e as capas de compartilhamento (Social preview) dos repositórios, todos no
mesmo padrão: fundo escuro, IBM Plex e destaque azul-petróleo (`#1b7f8f`).

## Como gerar

Pré-requisitos: Python 3 e Google Chrome. Se o Chrome estiver em outro caminho, informe pela variável
`CHROME`.

```bash
python identidade/gerar.py                    # banner e todas as capas
python identidade/gerar.py banner             # só o banner
python identidade/gerar.py painel-financeiro  # só a capa de um repositório
```

As imagens saem em `img/`. O Chrome renderiza os modelos em modo headless, então é preciso internet
para carregar a fonte IBM Plex e os ícones do [Lucide](https://lucide.dev/icons/).

## Projeto novo

1. Acrescente uma linha em `PROJETOS`, no `gerar.py`: repositório, título, descrição curta, stack
   separada por vírgulas, ícone do Lucide e categoria.
2. Gere a capa: `python identidade/gerar.py nome-do-repo`.
3. No GitHub, abra **Settings** do repositório e envie `img/nome-do-repo.png` em **Social preview**.
4. Se o projeto for para os destaques, inclua o card na tabela do `README.md` do perfil.

## Arquivos

```
capa.html    modelo da capa (1280x640)
banner.html  modelo do banner do perfil (1280x360)
gerar.py     lista dos projetos e geração das imagens
```
