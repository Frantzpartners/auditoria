import streamlit as st
import pandas as pd

st.set_page_config(page_title="Auditoria Blindada - Dagoberto Franz", layout="wide")

st.title("🛡️ Sistema de Fiscalização Robótica de Adquirência")
st.subheader("Operação Auditoria de Taxas — Dagoberto Franz")
st.write("---")

st.sidebar.header("🎯 Metas de Taxas Otimizadas")
st.sidebar.write("Defina as taxas alvo que você conquistará na matriz para o cliente:")

st.sidebar.subheader("💳 Cartões de Débito / Crédito")
tx_debito_alvo = st.sidebar.number_input("Débito Alvo (Visa/Master/Elo) (%)", value=1.25) / 100
tx_credito_alvo = st.sidebar.number_input("Crédito 1x Alvo (Visa/Master/Elo) (%)", value=1.50) / 100
tx_parcelado_alvo = st.sidebar.number_input("MDR Parcelado Alvo (%)", value=2.00) / 100

st.sidebar.subheader("🎫 Vouchers (Benefícios)")
tx_voucher_alvo = st.sidebar.number_input("Alimentação/Refeição Alvo (%)", value=3.50) / 100

st.sidebar.subheader("🛑 Outros Produtos")
receba_rapido_autorizado = st.sidebar.checkbox("Receba Rápido Autorizado no Contrato?", value=False)
custo_aluguel_alvo = st.sidebar.number_input("Meta de Aluguel de Máquinas (R$)", value=0.0)

st.header("📋 Diagnóstico de Arranjos de Pagamento do Cliente")
st.write("Insira as taxas reais praticadas atualmente pelo banco/credenciadora do lojista:")

tab_debito, tab_credito, tab_vouchers, tab_custom, tab_fixos = st.tabs([
    "🔵 Arranjos de Débito", "🟢 Arranjos de Crédito", "🟠 Vouchers / Benefícios", "➕ Customizar Nova Bandeira", "📟 Custos Fixos & Pix"
])

dados_auditoria = []

with tab_debito:
    st.write("#### Taxas Atuais de Débito")
    col1, col2, col3, col4 = st.columns(4)
    v_deb_visa = col1.number_input("Vol. Semanal Visa Débito (R$)", value=20000.0)
    tx_deb_visa = col1.number_input("Taxa Real Visa Débito (%)", value=2.25) / 100
    dados_auditoria.append({"Arranjo": "DEBITO", "Bandeira": "VISA", "Volume": v_deb_visa, "Taxa Real": tx_deb_visa, "Taxa Alvo": tx_debito_alvo})
    
    v_deb_master = col2.number_input("Vol. Semanal Master Débito (R$)", value=15000.0)
    tx_deb_master = col2.number_input("Taxa Real Master Débito (%)", value=2.25) / 100
    dados_auditoria.append({"Arranjo": "DEBITO", "Bandeira": "MASTERCARD", "Volume": v_deb_master, "Taxa Real": tx_deb_master, "Taxa Alvo": tx_debito_alvo})
    
    v_deb_elo = col3.number_input("Vol. Semanal Elo Débito (R$)", value=5000.0)
    tx_deb_elo = col3.number_input("Taxa Real Elo Débito (%)", value=2.50) / 100
    dados_auditoria.append({"Arranjo": "DEBITO", "Bandeira": "ELO", "Volume": v_deb_elo, "Taxa Real": tx_deb_elo, "Taxa Alvo": tx_debito_alvo})
    
    v_deb_diners = col4.number_input("Vol. Semanal Diners Débito (R$)", value=1000.0)
    tx_deb_diners = col4.number_input("Taxa Real Diners Débito (%)", value=2.80) / 100
    dados_auditoria.append({"Arranjo": "DEBITO", "Bandeira": "DINERS", "Volume": v_deb_diners, "Taxa Real": tx_deb_diners, "Taxa Alvo": tx_debito_alvo})

with tab_credito:
    st.write("#### Taxas Atuais de Crédito à Vista e Parcelado")
    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    v_cred_visa = col_c1.number_input("Vol. Semanal Visa Crédito 1x (R$)", value=25000.0)
    tx_cred_visa = col_c1.number_input("Taxa Real Visa Crédito 1x (%)", value=2.75) / 100
    dados_auditoria.append({"Arranjo": "CREDITO_1X", "Bandeira": "VISA", "Volume": v_cred_visa, "Taxa Real": tx_cred_visa, "Taxa Alvo": tx_credito_alvo})
    
    v_cred_master = col_c2.number_input("Vol. Semanal Master Crédito 1x (R$)", value=20000.0)
    tx_cred_master = col_c2.number_input("Taxa Real Master Crédito 1x (%)", value=2.75) / 100
    dados_auditoria.append({"Arranjo": "CREDITO_1X", "Bandeira": "MASTERCARD", "Volume": v_cred_master, "Taxa Real": tx_cred_master, "Taxa Alvo": tx_credito_alvo})
    
    v_cred_elo = col_c3.number_input("Vol. Semanal Elo Crédito 1x (R$)", value=8000.0)
    tx_cred_elo = col_c3.number_input("Taxa Real Elo Crédito 1x (%)", value=3.20) / 100
    dados_auditoria.append({"Arranjo": "CREDITO_1X", "Bandeira": "ELO", "Volume": v_cred_elo, "Taxa Real": tx_cred_elo, "Taxa Alvo": tx_credito_alvo})
    
    v_cred_amex = col_c4.number_input("Vol. Semanal Amex Crédito 1x (R$)", value=3000.0)
    tx_cred_amex = col_c4.number_input("Taxa Real Amex Crédito 1x (%)", value=3.99) / 100
    dados_auditoria.append({"Arranjo": "CREDITO_1X", "Bandeira": "AMEX", "Volume": v_cred_amex, "Taxa Real": tx_cred_amex, "Taxa Alvo": tx_credito_alvo})

with tab_vouchers:
    st.write("#### Taxas Atuais de Cartões de Benefício (Refeição/Alimentação)")
    col_v1, col_v2, col_v3 = st.columns(3)
    v_alelo = col_v1.number_input("Vol. Semanal Alelo (R$)", value=7000.0)
    tx_alelo = col_v1.number_input("Taxa Real Alelo (%)", value=5.50) / 100
    dados_auditoria.append({"Arranjo": "VOUCHER", "Bandeira": "ALELO", "Volume": v_alelo, "Taxa Real": tx_alelo, "Taxa Alvo": tx_voucher_alvo})
    
    v_sodexo = col_v2.number_input("Vol. Semanal Sodexo (R$)", value=6000.0)
    tx_sodexo = col_v2.number_input("Taxa Real Sodexo (%)", value=5.50) / 100
    dados_auditoria.append({"Arranjo": "VOUCHER", "Bandeira": "SODEXO", "Volume": v_sodexo, "Taxa Real": tx_sodexo, "Taxa Alvo": tx_voucher_alvo})
    
    v_ticket = col_v3.number_input("Vol. Semanal Ticket (R$)", value=4000.0)
    tx_ticket = col_v3.number_input("Taxa Real Ticket (%)", value=5.80) / 100
    dados_auditoria.append({"Arranjo": "VOUCHER", "Bandeira": "TICKET", "Volume": v_ticket, "Taxa Real": tx_ticket, "Taxa Alvo": tx_voucher_alvo})

with tab_custom:
    st.write("#### Espaço Aberto para Carregar Novas Bandeiras / Arranjos Customizados")
    nome_custom = st.text_input("Nome da Nova Bandeira / Voucher", value="VR Benefícios")
    tipo_custom = st.selectbox("Tipo de Arranjo", ["DÉBITO", "CRÉDITO 1X", "VOUCHER"])
    v_custom = st.number_input(f"Vol. Semanal de {nome_custom} (R$)", value=0.0)
    tx_custom_real = st.number_input(f"Taxa Real de {nome_custom} (%)", value=5.00) / 100
    
    alvo_c = tx_voucher_alvo if tipo_custom == "VOUCHER" else (tx_debito_alvo if tipo_custom == "DÉBITO" else tx_credito_alvo)
    
    if v_custom > 0:
        dados_auditoria.append({"Arranjo": tipo_custom, "Bandeira": nome_custom.upper(), "Volume": v_custom, "Taxa Real": tx_custom_real, "Taxa Alvo": alvo_c})
        st.success(f"✔️ {nome_custom} adicionado com sucesso ao fluxo de checagem!")

with tab_fixos:
    st.write("#### Custos Fixos Operacionais e Pix")
    col_f1, col_f2, col_f3 = st.columns(3)
    custo_aluguel_real = col_f1.number_input("Custo Semanal Real de Aluguel de Máquinas (R$)", value=150.0)
    v_pix = col_f2.number_input("Vol. Semanal de Pix Recebido na Maquininha (R$)", value=12000.0)
    tx_pix_real = col_f2.number_input("Taxa Real cobrada no Pix (%)", value=1.40) / 100
    
    v_parcelado_tt = col_f3.number_input("Vol. Semanal de Crédito Parcelado (R$)", value=30000.0)
    tx_antecipacao_real = col_f3.number_input("Taxa Real de Antecipação/Receba Rápido (%)", value=4.00) / 100

st.write("---")

if st.button("🚀 Rodar Fiscalização por Bandeira e Calcular Lucro"):
    st.write("### 🤖 Relatório Analítico de Irregularidades Tarifárias:")
    
    df_analise = pd.DataFrame(dados_auditoria)
    total_prejuizo_taxas = 0
    linhas_erros = []
    
    for index, row in df_analise.iterrows():
        if row["Taxa Real"] > row["Taxa Alvo"]:
            prejuizo = row["Volume"] * (row["Taxa Real"] - row["Taxa Alvo"])
            total_prejuizo_taxas += prejuizo
            linhas_erros.append({
                "Arranjo/Produto": f"{row['Arranjo']} ({row['Bandeira']})",
                "Volume Semanal": f"R$ {row['Volume']:.2f}",
                "Taxa Cobrada": f"{row['Taxa Real']*100:.2f}%",
                "Taxa Alvo (Dagoberto)": f"{row['Taxa Alvo']*100:.2f}%",
                "Vazamento Calculado": f"R$ {prejuizo:.2f}"
            })
            
    prejuizo_aluguel = max(0.0, custo_aluguel_real - custo_aluguel_alvo)
    prejuizo_pix = v_pix * tx_pix_real
    prejuizo_rr = 0 if receba_rapido_autorizado else (v_parcelado_tt * tx_antecipacao_real)
    
    total_vazamento_final = total_prejuizo_taxas + prejuizo_aluguel + prejuizo_pix + prejuizo_rr
    
    if linhas_erros:
        st.error("🚨 GORDURA DETECTADA NAS BANDEIRAS E VOUCHERS:")
        st.table(pd.DataFrame(linhas_erros))
    
    st.error("🚨 VAZAMENTOS EM CUSTOS OPERACIONAIS E PRODUTOS AUTOMÁTICOS:")
    st.warning(f"• **Aluguel de Máquinas:** R$ {prejuizo_aluguel:.2f} cobrados indevidamente (Sua meta é Zerar por TPV).")
    st.warning(f"• **Ralo do Pix Integrado:** R$ {prejuizo_pix:.2f} retidos pelo banco em transferências instantâneas.")
    if prejuizo_rr > 0:
        st.warning(f"• **Ralo do Receba Rápido:** R$ {prejuizo_rr:.2f} cobrados via antecipação forçada no parcelado.")
        
    st.write("---")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric(label="💰 Vazamento de Caixa Semanal Estancado (Lucro do Cliente)", value=f"R$ {total_vazamento_final:.2f}")
    with col_res2:
        st.metric(label="🤝 Sua Comissão de Performance Semanal (50% no Pix)", value=f"R$ {total_vazamento_final / 2:.2f}")
        
    st.success(f"🎯 Argumento Matador: Com a intervenção técnica da equipe Dagoberto Franz, o cliente economiza R$ {total_vazamento_final - (total_vazamento_final/2):.2f} limpos por semana e transfere R$ {total_vazamento_final / 2:.2f} de comissão por puro êxito.")
    
    st.button("📄 Exportar Relatório em PDF com Divisão por Bandeiras")
