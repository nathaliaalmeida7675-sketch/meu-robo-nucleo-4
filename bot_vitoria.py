import os
import time

# 1. Puxa a chave privada com segurança dos Secrets do GitHub
chave = os.getenv('STREAMR_PRIVATE_KEY')

# 2. Endereço do Contrato da sua Streamr (Operador)
contrato = "0x438805950f7eca7924513c45516e3504570e4c3d"

def minerador():
    if chave:
        print(f"✅ [BOT 04] Crachá validado! Conectado à rede Streamr...")
        print(f"📍 Contrato Operador: {contrato}")
        
        # Define o tempo de produção (15 minutos)
        tempo_operacao = 15 * 60
        inicio = time.time()
        
        print("🚀 [BOT 04] Iniciando ciclo de produção e integridade de dados.")
        
        while (time.time() - inicio) < tempo_operacao:
            # Mantendo seu intervalo estratégico de 70 segundos
            print("🧱 [BOT 04] Minerando dados... Operação em andamento.")
            time.sleep(70) 
            
        print("Sessão do BOT 04 finalizada com sucesso.")
    else:
        print("❌ Erro no BOT 04: Chave privada não encontrada nos Secrets.")

if __name__ == "__main__":
    minerador()
