import streamlit as st
import math

# =============================================================================
# НАСТРОЙКИ СТРАНИЦЫ
# =============================================================================
st.set_page_config(
    page_title="ФЭСТ — Подготовка к ЕГЭ по физике",
    page_icon="⚡",
    layout="centered"
)

# =============================================================================
# ФУНКЦИИ ПЕРЕВОДА В СИ
# =============================================================================
def to_si(value, unit):
    """Переводит величину в систему СИ"""
    prefixes = {
        'пико': 1e-12, 'нано': 1e-9, 'микро': 1e-6, 'милли': 1e-3,
        '': 1, 'кило': 1e3, 'мега': 1e6, 'гига': 1e9
    }
    return value * prefixes.get(unit, 1)

def format_si(value, unit):
    """Форматирует вывод с единицами измерения"""
    return f"{value:.4g} {unit}"

# =============================================================================
# МОДУЛЬ 1: ЭЛЕКТРОСТАТИКА
# =============================================================================
def module_electrostatics():
    st.header("⚡ Электростатика")
    
    task = st.selectbox(
        "Выберите задачу:",
        ["Закон Кулона", "Напряжённость поля", "Ёмкость конденсатора", "Энергия конденсатора"]
    )
    
    if task == "Закон Кулона":
        st.subheader("Расчёт силы взаимодействия зарядов")
        q1 = st.number_input("Заряд q1 (Кл)", value=1e-6, format="%.2e")
        q2 = st.number_input("Заряд q2 (Кл)", value=1e-6, format="%.2e")
        r = st.number_input("Расстояние r (м)", value=0.1)
        
        if st.button("Рассчитать"):
            k = 9e9  # Коэффициент пропорциональности
            F = k * abs(q1 * q2) / (r ** 2)
            
            st.success("### Решение:")
            st.latex(r"F = k \cdot \frac{|q_1 \cdot q_2|}{r^2}")
            st.write(f"**Дано:** q₁ = {q1} Кл, q₂ = {q2} Кл, r = {r} м")
            st.write(f"**Подстановка:** F = 9×10⁹ × |{q1} × {q2}| / {r}²")
            st.info(f"**Ответ:** F = {F:.4g} Н")
    
    elif task == "Напряжённость поля":
        st.subheader("Расчёт напряжённости электрического поля")
        q = st.number_input("Заряд q (Кл)", value=1e-6, format="%.2e")
        r = st.number_input("Расстояние r (м)", value=0.1)
        
        if st.button("Рассчитать"):
            k = 9e9
            E = k * abs(q) / (r ** 2)
            
            st.success("### Решение:")
            st.latex(r"E = k \cdot \frac{|q|}{r^2}")
            st.write(f"**Дано:** q = {q} Кл, r = {r} м")
            st.write(f"**Подстановка:** E = 9×10⁹ × |{q}| / {r}²")
            st.info(f"**Ответ:** E = {E:.4g} В/м")
    
    elif task == "Ёмкость конденсатора":
        st.subheader("Ёмкость плоского конденсатора")
        eps = st.number_input("Диэлектрическая проницаемость ε", value=1.0)
        S = st.number_input("Площадь пластин S (м²)", value=0.01, format="%.2e")
        d = st.number_input("Расстояние между пластинами d (м)", value=0.001)
        
        if st.button("Рассчитать"):
            eps0 = 8.85e-12
            C = eps0 * eps * S / d
            
            st.success("### Решение:")
            st.latex(r"C = \varepsilon_0 \cdot \varepsilon \cdot \frac{S}{d}")
            st.write(f"**Дано:** ε = {eps}, S = {S} м², d = {d} м")
            st.write(f"**Подстановка:** C = 8.85×10⁻¹² × {eps} × {S} / {d}")
            st.info(f"**Ответ:** C = {C:.4g} Ф")
    
    elif task == "Энергия конденсатора":
        st.subheader("Энергия заряженного конденсатора")
        C = st.number_input("Ёмкость C (Ф)", value=1e-6, format="%.2e")
        U = st.number_input("Напряжение U (В)", value=100.0)
        
        if st.button("Рассчитать"):
            W = 0.5 * C * (U ** 2)
            
            st.success("### Решение:")
            st.latex(r"W = \frac{C \cdot U^2}{2}")
            st.write(f"**Дано:** C = {C} Ф, U = {U} В")
            st.write(f"**Подстановка:** W = 0.5 × {C} × {U}²")
            st.info(f"**Ответ:** W = {W:.4g} Дж")

# =============================================================================
# МОДУЛЬ 2: ПОСТОЯННЫЙ ТОК
# =============================================================================
def module_dc_current():
    st.header("🔋 Постоянный ток")
    
    task = st.selectbox(
        "Выберите задачу:",
        ["Закон Ома (участок)", "Закон Ома (полная цепь)", "Мощность тока", "КПД источника"]
    )
    
    if task == "Закон Ома (участок)":
        st.subheader("Расчёт силы тока на участке цепи")
        U = st.number_input("Напряжение U (В)", value=12.0)
        R = st.number_input("Сопротивление R (Ом)", value=10.0)
        
        if st.button("Рассчитать"):
            I = U / R
            
            st.success("### Решение:")
            st.latex(r"I = \frac{U}{R}")
            st.write(f"**Дано:** U = {U} В, R = {R} Ом")
            st.write(f"**Подстановка:** I = {U} / {R}")
            st.info(f"**Ответ:** I = {I:.4g} А")
    
    elif task == "Закон Ома (полная цепь)":
        st.subheader("Расчёт силы тока в полной цепи")
        eps = st.number_input("ЭДС источника ε (В)", value=12.0)
        R = st.number_input("Внешнее сопротивление R (Ом)", value=10.0)
        r = st.number_input("Внутреннее сопротивление r (Ом)", value=1.0)
        
        if st.button("Рассчитать"):
            I = eps / (R + r)
            
            st.success("### Решение:")
            st.latex(r"I = \frac{\varepsilon}{R + r}")
            st.write(f"**Дано:** ε = {eps} В, R = {R} Ом, r = {r} Ом")
            st.write(f"**Подстановка:** I = {eps} / ({R} + {r})")
            st.info(f"**Ответ:** I = {I:.4g} А")
    
    elif task == "Мощность тока":
        st.subheader("Расчёт мощности электрического тока")
        I = st.number_input("Сила тока I (А)", value=2.0)
        U = st.number_input("Напряжение U (В)", value=12.0)
        
        if st.button("Рассчитать"):
            P = I * U
            
            st.success("### Решение:")
            st.latex(r"P = I \cdot U")
            st.write(f"**Дано:** I = {I} А, U = {U} В")
            st.write(f"**Подстановка:** P = {I} × {U}")
            st.info(f"**Ответ:** P = {P:.4g} Вт")
    
    elif task == "КПД источника":
        st.subheader("Расчёт КПД источника тока")
        R = st.number_input("Внешнее сопротивление R (Ом)", value=10.0)
        r = st.number_input("Внутреннее сопротивление r (Ом)", value=1.0)
        
        if st.button("Рассчитать"):
            eta = R / (R + r) * 100
            
            st.success("### Решение:")
            st.latex(r"\eta = \frac{R}{R + r} \cdot 100\%")
            st.write(f"**Дано:** R = {R} Ом, r = {r} Ом")
            st.write(f"**Подстановка:** η = {R} / ({R} + {r}) × 100%")
            st.info(f"**Ответ:** η = {eta:.2f} %")

# =============================================================================
# МОДУЛЬ 3: МАГНЕТИЗМ
# =============================================================================
def module_magnetism():
    st.header("🧲 Магнетизм")
    
    task = st.selectbox(
        "Выберите задачу:",
        ["Сила Ампера", "Сила Лоренца", "Магнитный поток"]
    )
    
    if task == "Сила Ампера":
        st.subheader("Расчёт силы Ампера")
        I = st.number_input("Сила тока I (А)", value=2.0)
        B = st.number_input("Индукция B (Тл)", value=0.1, format="%.2e")
        l = st.number_input("Длина проводника l (м)", value=0.5)
        alpha = st.number_input("Угол α (градусы)", value=90.0)
        
        if st.button("Рассчитать"):
            F = I * B * l * math.sin(math.radians(alpha))
            
            st.success("### Решение:")
            st.latex(r"F = I \cdot B \cdot l \cdot \sin\alpha")
            st.write(f"**Дано:** I = {I} А, B = {B} Тл, l = {l} м, α = {alpha}°")
            st.write(f"**Подстановка:** F = {I} × {B} × {l} × sin({alpha}°)")
            st.info(f"**Ответ:** F = {F:.4g} Н")
    
    elif task == "Сила Лоренца":
        st.subheader("Расчёт силы Лоренца")
        q = st.number_input("Заряд q (Кл)", value=1.6e-19, format="%.2e")
        v = st.number_input("Скорость v (м/с)", value=1e6, format="%.2e")
        B = st.number_input("Индукция B (Тл)", value=0.1, format="%.2e")
        alpha = st.number_input("Угол α (градусы)", value=90.0)
        
        if st.button("Рассчитать"):
            F = abs(q) * v * B * math.sin(math.radians(alpha))
            
            st.success("### Решение:")
            st.latex(r"F = |q| \cdot v \cdot B \cdot \sin\alpha")
            st.write(f"**Дано:** q = {q} Кл, v = {v} м/с, B = {B} Тл, α = {alpha}°")
            st.write(f"**Подстановка:** F = |{q}| × {v} × {B} × sin({alpha}°)")
            st.info(f"**Ответ:** F = {F:.4g} Н")
    
    elif task == "Магнитный поток":
        st.subheader("Расчёт магнитного потока")
        B = st.number_input("Индукция B (Тл)", value=0.1, format="%.2e")
        S = st.number_input("Площадь S (м²)", value=0.01, format="%.2e")
        alpha = st.number_input("Угол α (градусы)", value=0.0)
        
        if st.button("Рассчитать"):
            Phi = B * S * math.cos(math.radians(alpha))
            
            st.success("### Решение:")
            st.latex(r"\Phi = B \cdot S \cdot \cos\alpha")
            st.write(f"**Дано:** B = {B} Тл, S = {S} м², α = {alpha}°")
            st.write(f"**Подстановка:** Φ = {B} × {S} × cos({alpha}°)")
            st.info(f"**Ответ:** Φ = {Phi:.4g} Вб")

# =============================================================================
# МОДУЛЬ 4: ЭЛЕКТРОМАГНИТНАЯ ИНДУКЦИЯ
# =============================================================================
def module_emi():
    st.header("🔄 Электромагнитная индукция")
    
    task = st.selectbox(
        "Выберите задачу:",
        ["ЭДС индукции (Фарадей)", "ЭДС самоиндукции", "Энергия магнитного поля"]
    )
    
    if task == "ЭДС индукции (Фарадей)":
        st.subheader("Расчёт ЭДС электромагнитной индукции")
        dPhi = st.number_input("Изменение потока ΔΦ (Вб)", value=0.01, format="%.2e")
        dt = st.number_input("Время Δt (с)", value=0.1)
        
        if st.button("Рассчитать"):
            eps = abs(dPhi / dt)
            
            st.success("### Решение:")
            st.latex(r"|\varepsilon| = \left|\frac{\Delta\Phi}{\Delta t}\right|")
            st.write(f"**Дано:** ΔΦ = {dPhi} Вб, Δt = {dt} с")
            st.write(f"**Подстановка:** |ε| = |{dPhi} / {dt}|")
            st.info(f"**Ответ:** |ε| = {eps:.4g} В")
    
    elif task == "ЭДС самоиндукции":
        st.subheader("Расчёт ЭДС самоиндукции")
        L = st.number_input("Индуктивность L (Гн)", value=0.1, format="%.2e")
        dI = st.number_input("Изменение тока ΔI (А)", value=2.0)
        dt = st.number_input("Время Δt (с)", value=0.1)
        
        if st.button("Рассчитать"):
            eps = abs(L * dI / dt)
            
            st.success("### Решение:")
            st.latex(r"\varepsilon_s = \left|L \cdot \frac{\Delta I}{\Delta t}\right|")
            st.write(f"**Дано:** L = {L} Гн, ΔI = {dI} А, Δt = {dt} с")
            st.write(f"**Подстановка:** εₛ = |{L} × {dI} / {dt}|")
            st.info(f"**Ответ:** εₛ = {eps:.4g} В")
    
    elif task == "Энергия магнитного поля":
        st.subheader("Энергия магнитного поля катушки")
        L = st.number_input("Индуктивность L (Гн)", value=0.1, format="%.2e")
        I = st.number_input("Сила тока I (А)", value=2.0)
        
        if st.button("Рассчитать"):
            W = 0.5 * L * (I ** 2)
            
            st.success("### Решение:")
            st.latex(r"W = \frac{L \cdot I^2}{2}")
            st.write(f"**Дано:** L = {L} Гн, I = {I} А")
            st.write(f"**Подстановка:** W = 0.5 × {L} × {I}²")
            st.info(f"**Ответ:** W = {W:.4g} Дж")

# =============================================================================
# ГЛАВНОЕ МЕНЮ
# =============================================================================
def main():
    st.title("⚡ ФЭСТ — Физическая Экспертная Система Тестирования")
    st.markdown("**Приложение для подготовки к ЕГЭ по физике (Электродинамика)**")
    st.markdown("---")
    
    # Боковое меню
    st.sidebar.title("📚 Модули")
    module = st.sidebar.radio(
        "Выберите раздел:",
        ["Электростатика", "Постоянный ток", "Магнетизм", "Электромагнитная индукция"]
    )
    
    # Отображение выбранного модуля
    if module == "Электростатика":
        module_electrostatics()
    elif module == "Постоянный ток":
        module_dc_current()
    elif module == "Магнетизм":
        module_magnetism()
    elif module == "Электромагнитная индукция":
        module_emi()
    
    # Подвал
    st.markdown("---")
    st.caption("© 2026 ФЭСТ | Проект ученика 11 класса | Код открыт на GitHub")

if __name__ == "__main__":
    main()