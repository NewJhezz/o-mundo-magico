from app import app, home, cores, world
import os

def build_static():
    """
    Gera arquivos HTML estáticos a partir do aplicativo Flask.
    Isso permite abrir o site clicando diretamente nos arquivos HTML.
    """
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print("🔮 Iniciando ritual de petrificação (Gerando site estático)...")

    # 1. Cria a pasta 'build' se não existir
    if not os.path.exists('build'):
        os.makedirs('build')

    # Configura o contexto de REQUISIÇÃO (test_request_context) em vez de apenas app_context
    # Isso engana o Flask achando que existe um navegador acessando, permitindo usar url_for
    with app.test_request_context():
        # --- Gerar Home / Varinhas ---
        # Renderiza a home (Varinhas)
        content_woods = home()
        # Corrige links para funcionar offline/localmente
        content_woods = content_woods.replace('href="/static/', 'href="./static/')
        content_woods = content_woods.replace('href="/"', 'href="./index.html"')
        content_woods = content_woods.replace('href="/nucleos"', 'href="./nucleos.html"')
        content_woods = content_woods.replace('href="/mundo"', 'href="./mundo.html"')
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content_woods)
        print("✅ index.html gerado com sucesso!")

        # --- Gerar Núcleos ---
        content_cores = cores()
        # Mesmas correções
        content_cores = content_cores.replace('href="/static/', 'href="./static/')
        content_cores = content_cores.replace('href="/"', 'href="./index.html"')
        content_cores = content_cores.replace('href="/nucleos"', 'href="./nucleos.html"')
        content_cores = content_cores.replace('href="/mundo"', 'href="./mundo.html"')

        with open('nucleos.html', 'w', encoding='utf-8') as f:
            f.write(content_cores)
        print("✅ nucleos.html gerado com sucesso!")

        # --- Gerar Mundo ---
        content_world = world()
        # Mesmas correções
        content_world = content_world.replace('href="/static/', 'href="./static/')
        content_world = content_world.replace('href="/"', 'href="./index.html"')
        content_world = content_world.replace('href="/nucleos"', 'href="./nucleos.html"')
        content_world = content_world.replace('href="/mundo"', 'href="./mundo.html"')

        with open('mundo.html', 'w', encoding='utf-8') as f:
            f.write(content_world)
        print("✅ mundo.html gerado com sucesso!")

    print("\n✨ Feito! Agora você pode abrir 'index.html' diretamente.")

if __name__ == "__main__":
    build_static()
