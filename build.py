from app import app
import os

def build_static():
    """
    Gera arquivos HTML estáticos a partir do aplicativo Flask.
    """
    print("...Iniciando geracao do site estatico...")

    # 1. Cria a pasta 'build' se não existir
    if not os.path.exists('build'):
        os.makedirs('build')

    with app.test_request_context():
        # --- Helpers de correção de link ---
        def fix_links(content):
            content = content.replace('href="/static/', 'href="./static/')
            content = content.replace('href="/"', 'href="./index.html"')
            content = content.replace('href="/varinhas/origem"', 'href="./varinhas_origem.html"')
            content = content.replace('href="/varinhas/madeiras"', 'href="./varinhas_madeiras.html"')
            content = content.replace('href="/varinhas/nucleos"', 'href="./varinhas_nucleos.html"')
            content = content.replace('href="/varinhas"', 'href="./varinhas_madeiras.html"')
            content = content.replace('href="/mundo"', 'href="./index.html"')
            content = content.replace('href="/criaturas"', 'href="./criaturas.html"')
            content = content.replace('href="/sapos"', 'href="./sapos.html"')
            content = content.replace('href="/feiticos"', 'href="./feiticos.html"')
            return content

        # --- 1. Abertura (Mundo) ---
        from app import home
        content = home()
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(fix_links(content))
        print("OK: index.html (Home) gerado!")

        # --- 2. Varinhas: Origem ---
        from app import wands_origin
        content = wands_origin()
        with open('varinhas_origem.html', 'w', encoding='utf-8') as f:
            f.write(fix_links(content))
        print("OK: varinhas_origem.html gerado!")

        # --- 3. Varinhas: Madeiras ---
        from app import wands_woods
        content = wands_woods()
        with open('varinhas_madeiras.html', 'w', encoding='utf-8') as f:
            f.write(fix_links(content))
        print("OK: varinhas_madeiras.html gerado!")

        # --- 4. Varinhas: Núcleos ---
        from app import wands_cores
        content = wands_cores()
        with open('varinhas_nucleos.html', 'w', encoding='utf-8') as f:
            f.write(fix_links(content))
        print("OK: varinhas_nucleos.html gerado!")

        # --- 5. Criaturas ---
        from app import creatures
        content = creatures()
        with open('criaturas.html', 'w', encoding='utf-8') as f:
            f.write(fix_links(content))
        print("OK: criaturas.html gerado!")

        # --- 6. Sapos de Chocolate ---
        from app import frogs
        content = frogs()
        with open('sapos.html', 'w', encoding='utf-8') as f:
            f.write(fix_links(content))
        print("OK: sapos.html gerado!")

        # --- 7. Feitiços ---
        from app import spells
        content = spells()
        with open('feiticos.html', 'w', encoding='utf-8') as f:
            f.write(fix_links(content))
        print("OK: feiticos.html gerado!")

    print("CONCLUIDO: Abra 'index.html' para entrar no Mundo Magico.")

if __name__ == "__main__":
    build_static()
