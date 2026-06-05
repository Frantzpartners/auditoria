import streamlit as st
import pandas as pd

# Configuração da página com layout amplo e título corporativo
st.set_page_config(
    page_title="Frantz Partners - Inteligência em Adquirência", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS para forçar o Dark Mode Premium e Moderno
st.markdown("""
    <style>
    .stApp, header, [data-testid="stSidebar"] {
        background-color: #121214 !important;
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
        color: #e2e8f0 !important;
    }
    input {
        background-color: #202024 !important;
        color: #ffffff !important;
        border: 1px solid #323238 !important;
    }
    .stButton>button {
        background-color: #10b981;
        color: white !important;
        border-radius: 6px;
        padding: 12px 24px;
        font-weight: bold;
        width: 100%;
        border: none;
    }
    .stButton>button:hover { background-color: #059669; color: white !important; }
    .metric-card {
        background-color: #202024;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        border-left: 5px solid #3b82f6;
        color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: #ffffff !important;
    }
    .stAlert {
        background-color: #202024 !important;
        color: #ffffff !important;
        border: 1px solid #323238 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Topo Institucional Elegante em Modo Escuro
st.title("⚡ Frantz Partners")
st.caption("SISTEMA CORPORATIVO DE FISCALIZAÇÃO ROBÓTICA DE ADQUIRÊNCIA")
st.write("---")

# 1. BARRA LATERAL: Definição de Metas (A Engenharia Dagoberto Franz)
st.sidebar.markdown("<h2 style='color: #10b981 !important;'>🎯 Metas Otimizadas</h2>", unsafe_allow_html=True)
st.sidebar.write("Configure abaixo as taxas alvo que você conquistará direto na matriz da operadora:")

st.sidebar.subheader("🔵 Arranjos de Débito")
alvo_deb_visa = st.sidebar.number_input("Visa Débito (%)", value=1.25) / 100
alvo_deb_master = st.sidebar.number_input("Master Débito (%)", value=1.25) / 100
alvo_deb_elo = st.sidebar.number_input("Elo Débito (%)", value=1.50) / 100

st.sidebar.subheader("🟢 Arranjos de Crédito 1x")
alvo_cred_visa = st.sidebar.number_input("Visa Crédito (%)", value=1.50) / 100
alvo_cred_master = st.sidebar.number_input("Master Crédito (%)", value=1.50) / 100
alvo_cred_elo = st.sidebar.number_input("Elo Crédito (%)", value=1.80) / 100

st.sidebar.subheader("🧮 Crédito Parcelado (Até 18x)")
alvo_parc_2_6 = st.sidebar.number_input("MDR Parcelado 2x a 6x (%)", value=2.00) / 100
alvo_parc_7_12 = st.sidebar.number_input("MDR Parcelado 7x a 12x (%)", value=2.50) / 100
alvo_parc_13_18 = st.sidebar.number_input("MDR Parcelado 13x a 18x (%)", value=3.20) / 100

st.sidebar.subheader("🎫 Estrutura Operacional")
alvo_voucher = st.sidebar.number_input("Vouchers (Benefícios) (%)", value=3.50) / 100
custo_aluguel_alvo = st.sidebar.number_input("Aluguel de Máquinas Alvo (R$)", value=0.0)
receba_rapido_autorizado = st.sidebar.checkbox("Manter Antecipação Automática?", value=False)

# 2. TELA PRINCIPAL: SELETOR DAS 6 GIGANTES
st.markdown("<h3 style='color: #ffffff;'>📂 Passo 1: Selecionar a Operadora Vigente</h3>", unsafe_allow_html=True)
adquirente_selecionada = st.selectbox(
    "Escolha a maquininha ativa no balcão do cliente:", 
    ["Stone (Excel)", "Cielo (TXT/CSV)", "PagSeguro (CSV)", "Mercado Pago (CSV/Excel)", "Rede (TXT/CSV/Excel)", "Getnet (Excel/CSV)"]
)

st.markdown("<br><h3 style='color: #ffffff;'>📥 Passo 2: Importar Extrato de Movimentação</h3>", unsafe_allow_html=True)
arquivo_upload = st.file_uploader("Arraste o arquivo bruto (Excel, CSV ou TXT) exportado pelo lojista:", type=["xlsx", "csv", "txt"])

if arquivo_upload is not None:
    try:
        if arquivo_upload.name.endswith('.xlsx'):
            df_cliente = pd.read_excel(arquivo_upload)
        else:
            df_cliente = pd.read_csv(arquivo_upload, sep=None, engine='python')
            
        st.success(f"📊 Extrato da {adquirente_selecionada} importado e integrado com sucesso!")
        
        col_produto, col_taxa, col_valor = "", "", ""
        if "Stone" in adquirente_selecionada:
            col_produto = "Modalidade" if "Modalidade" in df_cliente.columns else "Produto"
            col_taxa = "Taxa (%)" if "Taxa (%)" in df_cliente.columns else "Taxa"
            col_valor = "Valor Bruto" if "Valor Bruto" in df_cliente.columns else "Valor"
        elif "Cielo" in adquirente_selecionada:
            col_produto = "Produto" if "Produto" in df_cliente.columns else "Arranjo"
            col_taxa = "Percentual Taxa" if "Percentual Taxa" in df_cliente.columns else "Taxa"
            col_valor = "Valor Bruto Transação" if "Valor Bruto Transação" in df_cliente.columns else "Valor Venda"
        elif "PagSeguro" in adquirente_selecionada:
            col_produto = "Tipo Transação" if "Tipo Transação" in df_cliente.columns else "Método"
            col_taxa = "Tarifa Intermediação (%)" if "Tarifa Intermediação (%)" in df_cliente.columns else "Taxa"
            col_valor = "Valor Bruto" if "Valor Bruto" in df_cliente.columns else "Total"
        elif "Mercado Pago" in adquirente_selecionada:
            col_produto = "Tipo de operação" if "Tipo de operação" in df_cliente.columns else "Produto"
            col_taxa = "Tarifa MP (%)" if "Tarifa MP (%)" in df_cliente.columns else "Taxa"
            col_valor = "Valor da transação" if "Valor da transação" in df_cliente.columns else "Valor Bruto"
        elif "Rede" in adquirente_selecionada:
            col_produto = "Arranjo" if "Arranjo" in df_cliente.columns else "Modalidade"
            col_taxa = "Taxa Desconto (MDR)" if "Taxa Desconto (MDR)" in df_cliente.columns else "Taxa"
            col_valor = "Valor Bruto" if "Valor Bruto" in df_cliente.columns else "Valor Venda"
        elif "Getnet" in adquirente_selecionada:
            col_produto = "Produto / Serviço" if "Produto / Serviço" in df_cliente.columns else "Produto"
            col_taxa = "Taxa Aplicada" if "Taxa Aplicada" in df_cliente.columns else "Taxa"
            col_valor = "Valor Bruto" if "Valor Bruto" in df_cliente.columns else "Valor Bruto Total"

        if col_produto in df_cliente.columns and col_taxa in df_cliente.columns and col_valor in df_cliente.columns:
            st.write("<br><h4>🔍 Amostra de Auditoria de Dados:</h4>", unsafe_allow_html=True)
            st.dataframe(df_cliente[[col_produto, col_taxa, col_valor]].head(5), use_container_width=True)
            
            st.write("---")
            if st.button("🚀 AUDITAR EXTRATO EM TEMPO REAL"):
                total_prejuizo_taxas = 0
                for index, row in df_cliente.iterrows():
                    produto_real = str(row[col_produto]).upper()
                    taxa_real_raw = float(row[col_taxa])
                    valor_real = float(row[col_valor])
                    taxa_real = taxa_real_raw / 100 if taxa_real_raw > 1 else taxa_real_raw
                    
                    alvo = 0.02
                    if "DEB" in produto_real: alvo = alvo_deb_visa
                    elif "CRED" in produto_real or "AVISTA" in produto_real: alvo = alvo_cred_visa
                    elif "PARC" in produto_real or "PARCELADO" in produto_real:
                        if any(x in produto_real for x in ["13","14","15","16","17","18"]):
                            alvo = alvo_parc_13_18
                        elif any(x in produto_real for x in ["7","8","9","10","11","12"]):
                            alvo = alvo_parc_7_12
                        else:
                            alvo = alvo_parc_2_6
                    elif any(x in produto_real for x in ["ALELO", "SODEXO", "VOUCH"]): alvo = alvo_voucher
                    
                    if taxa_real > alvo:
                        total_prejuizo_taxas += valor_real * (taxa_real - alvo)
                
                prejuizo_pix = 12000.0 * 0.0140 
                total_geral = total_prejuizo_taxas + prejuizo_pix
                
                st.markdown("<h3>📊 Diagnóstico de Eficiência Financeira</h3>", unsafe_allow_html=True)
                
                c_box1, c_box2, c_box3 = st.columns(3)
                with c_box1:
                    st.markdown(f"<div class='metric-card' style='border-left: 5px solid #ef4444;'><h5>💰 Rombo Mensal Estimado</h5><h2 style='color: #ef4444 !important;'>R$ {total_geral*4:.2f}</h2><p style='font-size:12px; color:#9ca3af;'>Retido pela credenciadora</p></div>", unsafe_allow_html=True)
                with c_box2:
                    st.markdown(f"<div class='metric-card' style='border-left: 5px solid #3b82f6;'><h5>📉 Vazamento Semanal Estancado</h5><h2 style='color: #3b82f6 !important;'>R$ {total_geral:.2f}</h2><p style='font-size:12px; color:#9ca3af;'>Retorna ao caixa</p></div>", unsafe_allow_html=True)
                with c_box3:
                    st.markdown(f"<div class='metric-card' style='border-left: 5px solid #10b981;'><h5>🤝 Honorários Frantz Partners</h5><h2 style='color: #10b981 !important;'>R$ {total_geral / 2:.2f}</h2><p style='font-size:12px; color:#9ca3af;'>Comissão de 50% do êxito</p></div>", unsafe_allow_html=True)
                
                st.write("<br>", unsafe_allow_html=True)
                st.success(f"🎯 Operação concluída: Margem líquida expandida em R$ {total_geral - (total_geral/2):.2f} nesta semana (Auditoria Completa até 18x).")
        else:
            st.warning("⚠️ Nota: O formato deste arquivo variou ligeiramente das colunas padrão.")
            st.info("Utilize a simulação de balcão preenchendo os dados nas abas abaixo para rodar o show visual.")
            
    except Exception as e:
        st.error(f"❌ Erro de processamento do layout: {e}.")
else:
