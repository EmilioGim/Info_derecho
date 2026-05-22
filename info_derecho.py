import streamlit as st

st.set_page_config(page_title="Software y Derecho · Demo", layout="wide")

st.markdown("""
<style>
body { font-family: 'Segoe UI', sans-serif; }
.caja { background:#f0f4ff; border-left:4px solid #2E5FA3; padding:12px 16px; border-radius:6px; margin:8px 0; }
.rojo { background:#fff0f0; border-left:4px solid #e63946; padding:12px 16px; border-radius:6px; margin:8px 0; }
.verde { background:#f0fff4; border-left:4px solid #2a9d8f; padding:12px 16px; border-radius:6px; margin:8px 0; }
.amarillo { background:#fffbe6; border-left:4px solid #f4a261; padding:12px 16px; border-radius:6px; margin:8px 0; }
code { background:#1e1e2e; color:#cdd6f4; padding:10px; border-radius:6px; display:block; font-size:0.85rem; line-height:1.6; }
</style>
""", unsafe_allow_html=True)

st.title("⚖️ Software y Derecho — Demo Ingeniería Informática")
st.caption("Extensión Universitaria · Legislación y Ética Profesional · Para estudiantes de Derecho")

tab1, tab2, tab3 = st.tabs([
    "🔬 Código Fuente vs Ejecutable",
    "📄 Contratos Informáticos",
    "🏛️ Caso Real: Atlas vs IIT"
])

# ══════════════════════════════════════════
# TAB 1 — CÓDIGO FUENTE VS EJECUTABLE
# ══════════════════════════════════════════
with tab1:
    st.subheader("¿Qué protege exactamente la Ley 1328/98?")

    st.markdown("""
    <div class='caja'>
    <b>Ley 1328/98 · Art. 5 — Paraguay:</b> El software está protegido como obra literaria.
    La protección recae sobre el <b>código fuente y el código objeto (ejecutable)</b>.
    Pero desde Ingeniería, son dos cosas muy distintas.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📝 Código Fuente")
        st.markdown("""
        <div class='verde'>
        Escrito por el programador en lenguaje humano-legible.<br>
        Contiene la <b>lógica, las decisiones de diseño, los algoritmos</b>.<br>
        Es como el <b>manuscrito original</b> de un libro.<br><br>
        → Aquí está el <b>valor intelectual real</b>.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Ejemplo real en Python:**")
        st.code("""# Calcular interés bancario
def calcular_interes(capital, tasa, años):
    return capital * (1 + tasa) ** años

resultado = calcular_interes(1000000, 0.05, 3)
print(f"Total: {resultado} Gs.")""", language="python")

    with col2:
        st.markdown("### ⚙️ Código Ejecutable (Objeto)")
        st.markdown("""
        <div class='rojo'>
        Lo que la computadora realmente ejecuta.<br>
        <b>Ilegible para humanos</b> — es una secuencia de instrucciones en binario.<br>
        Es como la <b>partitura impresa en código morse</b>.<br><br>
        → Se puede <b>usar</b> pero no se puede <b>entender ni modificar</b>.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**El mismo programa compilado (fragmento):**")
        st.code("""4d 5a 90 00 03 00 00 00
04 00 00 00 ff ff 00 00
b8 00 00 00 00 00 00 00
40 00 00 00 00 00 00 00
[...miles de líneas de números hexadecimales...]
Ininteligible sin el código fuente.""")

    st.divider()
    st.markdown("### 🎯 ¿Por qué importa esto en un contrato?")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <div class='amarillo'>
        <b>Empresa contrata software de gestión.</b><br><br>
        Le entregan el ejecutable (.exe). El sistema funciona.<br><br>
        5 años después el proveedor cierra. Nadie tiene el código fuente.<br><br>
        <b>La empresa no puede modificarlo, ni contratar a otro programador para actualizarlo.</b><br><br>
        ¿El contrato especificaba entrega del código fuente? Si no lo dice → el proveedor no está obligado.
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class='verde'>
        <b>Cláusula crítica que todo contrato de software debe tener:</b><br><br>
        "El proveedor entregará el código fuente completo, comentado y compilable,
        junto con la documentación técnica, al momento de la entrega final
        y/o rescisión del contrato."<br><br>
        Sin esta cláusula → el cliente queda <b>rehén tecnológico</b> del proveedor.
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### 🔍 Interactivo: ¿Qué recibió el cliente?")
    entrega = st.radio("En el contrato dice que se entrega:", [
        "El software funcionando",
        "El software y su código fuente",
        "Los archivos .exe y .dll",
        "Todo el proyecto de desarrollo"
    ])
    if entrega == "El software funcionando":
        st.markdown("<div class='rojo'>⚠️ <b>RIESGO ALTO:</b> 'Software funcionando' = solo ejecutable. Sin código fuente. El cliente no puede modificar nada sin el proveedor.</div>", unsafe_allow_html=True)
    elif entrega == "El software y su código fuente":
        st.markdown("<div class='verde'>✅ <b>CORRECTO:</b> Esta cláusula protege al cliente. Tiene la obra completa y puede contratar a cualquier programador para modificarla.</div>", unsafe_allow_html=True)
    elif entrega == "Los archivos .exe y .dll":
        st.markdown("<div class='rojo'>⚠️ <b>RIESGO ALTO:</b> .exe y .dll son ejecutables compilados. Inmodificables. Sin código fuente = sin control técnico.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='amarillo'>⚠️ <b>AMBIGUO:</b> 'Todo el proyecto' puede interpretarse de varias formas. Debe especificarse qué incluye: código fuente, bases de datos, documentación, credenciales.</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════
# TAB 2 — CONTRATOS INFORMÁTICOS
# ══════════════════════════════════════════
with tab2:
    st.subheader("Árbol de decisión: ¿Qué tipo de contrato es?")

    st.markdown("""
    <div class='caja'>
    En Paraguay no existe un código de contratos informáticos específico.
    Se aplican el <b>Código Civil (Ley 1183/85)</b>, la <b>Ley 1328/98</b> (derechos de autor sobre software)
    y principios generales de contratos de locación de obra y servicios.
    </div>
    """, unsafe_allow_html=True)

    tipo = st.selectbox("¿Qué se está contratando?", [
        "— Seleccionar —",
        "Desarrollo de software a medida",
        "Licencia de software existente",
        "Prestación de servicios de mantenimiento",
        "Hosting / infraestructura",
        "Consultoría tecnológica"
    ])

    if tipo == "Desarrollo de software a medida":
        st.markdown("""
        <div class='amarillo'>
        <h4>📋 Contrato de Desarrollo a Medida</h4>
        Similar a <b>locación de obra</b> (Cód. Civil Art. 848 y ss.)<br><br>
        <b>Cláusulas críticas desde Ingeniería:</b>
        </div>
        """, unsafe_allow_html=True)

        clausulas = {
            "Propiedad del código fuente": "¿Quién es dueño? Por defecto en Ley 1328: el AUTOR (programador). Si el cliente quiere ser dueño, debe pactarse EXPRESAMENTE.",
            "Especificaciones técnicas (SRS)": "El documento de requerimientos define QUÉ se construye. Sin él, no hay forma de probar incumplimiento.",
            "Entornos de prueba y aceptación": "Criterios técnicos objetivos para decir que el software 'funciona'. Sin esto, el cliente puede rechazar sin justificación.",
            "Escrow de código fuente": "Depósito del código en poder de un tercero neutral. Se libera si el proveedor desaparece o incumple.",
            "Garantía post-entrega": "Período durante el cual el proveedor corrige errores sin costo. Debe especificar qué es 'error' y qué es 'nueva funcionalidad'.",
        }

        for clausula, explicacion in clausulas.items():
            with st.expander(f"📌 {clausula}"):
                st.write(explicacion)

    elif tipo == "Licencia de software existente":
        st.markdown("""
        <div class='caja'>
        <h4>📋 Contrato de Licencia (EULA)</h4>
        El proveedor <b>NO vende</b> el software. Vende el <b>derecho de uso</b>.<br><br>
        Desde Ingeniería, esto tiene implicancias concretas:
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - **Licencia monopuesto vs multiusuario**: cuántas instalaciones simultáneas permite
        - **On-premise vs SaaS**: el software corre en tu servidor o en el del proveedor
        - **Actualizaciones incluidas o pagas**: ¿la versión 2.0 está cubierta o es contrato nuevo?
        - **Qué pasa si el proveedor cierra**: ¿tenés acceso al código fuente? (cláusula de escrow)
        """)

    elif tipo == "Prestación de servicios de mantenimiento":
        st.markdown("""
        <div class='verde'>
        <h4>📋 Contrato de Mantenimiento</h4>
        Dos tipos técnicamente distintos — el contrato debe especificar cuál:
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Mantenimiento Correctivo**")
            st.write("Corregir errores (bugs) del sistema existente. El sistema no hace lo que debía hacer.")
        with col2:
            st.markdown("**Mantenimiento Evolutivo**")
            st.write("Agregar nuevas funcionalidades. El sistema hace lo que debía, pero el cliente quiere más. Esto es desarrollo nuevo y debería cotizarse aparte.")

    elif tipo != "— Seleccionar —":
        st.markdown("<div class='caja'>Seleccionaste un tipo de contrato válido. En una sesión completa desarrollaríamos las cláusulas específicas.</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("### ⚠️ La pregunta del millón: ¿Quién es dueño del software?")
    st.markdown("""
    <div class='rojo'>
    <b>Ley 1328/98 · Art. 8:</b> En ausencia de estipulación contractual, 
    los derechos sobre el software creado por un empleado en el ejercicio de sus funciones 
    pertenecen al <b>empleador</b>.<br><br>
    Pero si es un <b>contratista independiente</b> (freelancer), los derechos son del <b>autor</b> 
    salvo pacto en contrario.<br><br>
    <b>Conclusión práctica:</b> Todo contrato de desarrollo debe tener una cláusula de 
    <i>cesión de derechos patrimoniales</i> explícita. Si no la tiene, hay un problema.
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# TAB 3 — CASO ATLAS vs IIT
# ══════════════════════════════════════════
with tab3:
    st.subheader("🏛️ Caso Banco Atlas S.A. vs Instituto Itaipú de Tecnología (IIT)")
    st.caption("Caso de referencia en Paraguay sobre propiedad de software — analizado desde Ingeniería")

    st.markdown("""
    <div class='amarillo'>
    ⚠️ <b>Nota:</b> Este caso se analiza con fines educativos, desde la perspectiva técnica-informática.
    El análisis jurídico completo corresponde a los profesionales del Derecho.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Los hechos técnicos")

    hechos = {
        "La relación contractual": """
        Banco Atlas contrató al IIT para desarrollar un sistema informático bancario a medida.
        Se trataba de software crítico para la operación del banco.
        **Desde Ingeniería**: un sistema bancario core puede tener entre 500.000 y varios millones de líneas de código.
        Es una obra de enorme complejidad técnica.
        """,
        "El objeto del conflicto: el código fuente": """
        El núcleo del conflicto era técnico: **¿a quién pertenece el código fuente?**
        
        - El banco alegaba haber pagado por el desarrollo = ser dueño de la obra.
        - El IIT alegaba ser el autor = tener derechos sobre el código.
        
        **Desde Ingeniería**: esto es exactamente la distinción entre *obra por encargo* 
        y *producto propio*. El contrato original no tenía cláusula clara de cesión de derechos.
        """,
        "El problema de la dependencia tecnológica": """
        Cuando se deterioró la relación comercial, el banco quedó en una posición crítica:
        
        - Tenía el sistema funcionando (ejecutable)
        - No tenía certeza legal sobre el código fuente
        - No podía contratar a otro proveedor sin resolver la disputa de propiedad
        
        **Desde Ingeniería**: esto se llama *vendor lock-in* combinado con disputa de IP.
        Es el peor escenario operativo para una entidad bancaria.
        """,
        "La lección técnico-legal": """
        El caso ilustra que en contratos de software, los conceptos técnicos tienen 
        consecuencias legales directas:
        
        1. **Código fuente ≠ ejecutable** → protecciones distintas
        2. **Pagar el desarrollo ≠ ser dueño** → requiere cesión expresa
        3. **Sistema funcionando ≠ independencia tecnológica** → el código fuente es la llave
        """,
    }

    for titulo, contenido in hechos.items():
        with st.expander(f"📂 {titulo}"):
            st.markdown(contenido)

    st.divider()
    st.markdown("### 🧩 El mapa técnico del conflicto")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='caja'>
        <b>Lo que el Banco tenía</b><br><br>
        ✅ Sistema funcionando<br>
        ✅ Facturas pagadas<br>
        ❌ Cláusula de cesión de código<br>
        ❌ Escrow del código fuente<br>
        ❌ Documentación técnica propia
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='amarillo'>
        <b>Lo que faltó en el contrato</b><br><br>
        📌 Cesión de derechos patrimoniales<br>
        📌 Entrega obligatoria del código fuente<br>
        📌 Propiedad de la base de datos<br>
        📌 Documentación técnica como entregable<br>
        📌 Cláusula de escrow
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='verde'>
        <b>Qué dice la Ley 1328/98</b><br><br>
        Art. 8: Sin pacto expreso,<br>
        los derechos son del autor.<br><br>
        El pago no transfiere<br>
        automáticamente la propiedad<br>
        intelectual del software.
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### 💬 Para reflexionar con el auditorio")
    st.markdown("""
    <div class='rojo'>
    <b>Pregunta técnica con respuesta legal:</b><br><br>
    Si mañana el IIT hubiera modificado una línea del código fuente y lo hubiera registrado 
    en DINAPI como versión nueva, ¿el Banco Atlas podría seguir usando el sistema original 
    sin infringir derechos de autor?<br><br>
    Desde Ingeniería: técnicamente sí, el ejecutable que ya tenían seguiría funcionando.<br>
    Desde el Derecho: depende de si la licencia de uso también era parte del conflicto.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='caja'>
    <b>¿Qué es DINAPI y qué protege?</b><br><br>
    La Dirección Nacional de Propiedad Intelectual (DINAPI) es el organismo paraguayo 
    que registra obras protegidas por derechos de autor, incluyendo software.<br><br>
    Desde Ingeniería: el registro en DINAPI no crea el derecho — la obra está protegida 
    desde su creación (Ley 1328, Art. 5). El registro sirve como <b>prueba de autoría y fecha</b>.<br><br>
    En el contexto del caso: registrar el código fuente en DINAPI antes de un conflicto 
    es la diferencia entre tener prueba y no tenerla.
    </div>
    """, unsafe_allow_html=True)