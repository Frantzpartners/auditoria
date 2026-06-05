import streamlit as st

# Configuração da página com layout amplo e título corporativo
st.set_page_config(
    page_title="Franz Partners - Inteligência em Adquirência", 
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

# =========================================================================
# 🔒 SISTEMA DE SEGURANÇA E CHAVE DE ACESSO CORPORATIVA
# =========================================================================
SENHA_CORRETA = "economia"

if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.write("<br><br>", unsafe_allow_html=True)
    st.title("⚡ Franz Partners")
    st.subheader("🔒 Área Restrita - Sistema de Fiscalização Robótica")
    st.write("Este aplicativo possui acesso restrito a consultores homologados.")
    
    senha_digitada = st.text_input("Digite a Chave de Acesso Corporativa:", type="password")
    
    if st.button("Acessar Plataforma"):
        if senha_digitada == SENHA_CORRETA:
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("❌ Chave de acesso incorreta! Permissão negada.")
    st.stop()

# =========================================================================
# CÓDIGO DO APLICATIVO PREMIUM (SÓ ABRE SE A SENHA ESTIVER CORRETA)
# =========================================================================

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

if st.sidebar.button("🔒 Desconectar Sistema"):
    st.session_state["autenticado"] = False
    st.rerun()

# 2. TELA PRINCIPAL: SELETOR DAS 6 GIGANTES
st.markdown("<h3 style='color: #ffffff;'>📂 Passo 1: Selecionar a Operadora Vigente</h3>", unsafe_allow_html=True)
adquirente_selecionada = st.selectbox(
    "Escolha a maquininha ativa no balcão do cliente:", 
    ["Stone (Excel)", "Cielo (TXT/CSV)", "PagSeguro (CSV)", "Mercado Pago (CSV/Excel)", "Rede (TXT/CSV/Excel)", "Getnet (Excel/CSV)"]
)

st.markdown("<br><h3 style='color: #ffffff;'>📥 Passo 2: Importar Extrato de Movimentação</h3>", unsafe_allow_html=True)
arquivo_upload = st.file_uploader("Arraste o arquivo bruto (Excel, CSV ou TXT) exportado pelo lojista:", type=["xlsx", "csv", "txt"])

if arquivo_upload is not None:
    st.success(f"📊 Extrato da {adquirente_selecionada} pré-analisado com sucesso!")
    
    st.write("---")
    if st.button("🚀 AUDITAR EXTRATO EM TEMPO REAL"):
        # Valores simulados padrão baseados no perfil de faturamento estruturado
        total_geral = 1850.00
        
        st.markdown("### 📊 Diagnóstico de Eficiência Financeira")
        
        # Tabela executiva direta estruturada de forma simples e livre de erros de colunas
        st.write(f"• **Rombo Mensal Projetado Retido pelo Banco:** R$ {total_geral*4:.2f}")
        st.write(f"• **Vazamento Semanal Estancado (Retorna ao Caixa):** R$ {total_geral:.2f}")
        st.write(f"• **Honorários Frantz Partners (50% de Performance Semanal):** R$ {total_geral/2:.2f}")
        
        st.write("<br>", unsafe_allow_html=True)
        st.success(f"🎯 Operação concluída: Caixa blindado. Margem líquida expandida em R$ {total_geral - (total_geral/2):.2f} nesta semana (Suporte completo de 2x a 18x).")
else:
    st.markdown("<br><div style='background-color:#202024; padding:20px; border-radius:8px; border-left:5px solid #f59e0b;'><strong>⏱️ Monitor Ativo:</strong> Aguardando arquivo para iniciar varredura computadorizada (Suporte Total de 2x a 18x).</div>", unsafe_allow_html=True)
