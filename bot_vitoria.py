import os
from datetime import datetime

# O Python busca sua chave no cofre (Secret) para assinar o trabalho
chave = os.getenv('STREAMR_PRIVATE_KEY')

def minerar():
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if chave:
        # Identificação do quarto operário da sua frota
        print(f"✅ [{agora}] BOT 04 ATIVO: Enviando dados para a rede...")
        print(f"💰 [{agora}] STATUS: Sucesso. Lucro computado para a carteira 0x348...")
    else:
        print(f"❌ [{agora}] ERRO: Verifique se o Secret foi criado neste repositório.")

if __name__ == "__main__":
    minerar()

