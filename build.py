from app import app
import os

def build_static():
    """
    Gera arquivos HTML estáticos a partir do aplicativo Flask.
    """
    print("🔮 Iniciando ritual de petrificação (Gerando site estático)...")

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
            content = content.replace('href="/varinhas"', 'href="./varinhas_origem.html"')
            return content

        # --- 1. Abertura (Mundo) ---
        from app import home
        content = home()
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content_world)
        print("✅ mundo.html gerado com sucesso!")

    print("\n✨ Feito! Agora você pode abrir 'index.html' diretamente.")

if __name__ == "__main__":
    build_static()
