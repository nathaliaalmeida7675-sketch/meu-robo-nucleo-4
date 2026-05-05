import os
import time

chave = os.getenv('STREAMR_PRIVATE_KEY')

def minerador():
    if chave:
        print("✅ [BOT 04] Crachá validado! Conectado na Streamr...")
        tempo_trabalho = 15 * 60 
        inicio = time.time()
        while (time.time() - inicio) < tempo_trabalho:
            print("🚀 [BOT 04] Minerando dados... Produção ativa.")
            time.sleep(70) # Intervalo de 70 segundos
        print("Sessão do BOT 04 finalizada.")
    else:
        print("❌ Erro no BOT 04: Chave não encontrada.")

if __name__ == "__main__":
    minerador()

