import streamlit as st
import math

# =============================================================================
# НАСТРОЙКИ СТРАНИЦЫ
# =============================================================================
st.set_page_config(
    page_title="ФЭСТ — Подготовка к ЕГЭ по физике",
    page_icon="⚡",
    layout="wide"
)

# =============================================================================
# МОДУЛЬ 1: ЭЛЕКТРОСТАТИКА (8 задач)
# =============================================================================
def module_electrostatics():
    st.header("⚡ Электростатика")
    
    task = st.selectbox(
        "Выберите задачу:",
        [
            "Закон Кулона",
            "Напряжённость поля точечного заряда",
            "Потенциал электрического поля",
            "Работа электрического поля",
            "Ёмкость плоского конденсатора",
            "Энергия конденсатора",
            "Соединение конденсаторов",
            "Напряжённость между пластинами"
        ]
    )
    
    if task == "Закон Кулона":
        st.subheader("Расчёт силы взаимодействия зарядов")
        q1 = st.number_input("Заряд q1 (Кл)", value=1e-6, format="%.2e")
        q2 = st.number_input("Заряд q2 (Кл)", value=1e-6, format="%.2e")
        r = st.number_input("Расстояние r (м)", value=0.1)
        
        if st.button("Рассчитать", key="coulomb"):
            k = 9e9
            F = k * abs(q1 * q2) / (r ** 2)
            st.success("### Решение:")
            st.latex(r"F = k \cdot \frac{|q_1 \cdot q_2|}{r^2}")
            st.write(f"**Дано:** q₁ = {q1} Кл, q₂ = {q2} Кл, r = {r} м")
            st.write(f"**Подстановка:** F = 9×10⁹ × |{q1} × {q2}| / {r}²")
            st.info(f"**Ответ:** F = {F:.4g} Н")
    
    elif task == "Напряжённость поля точечного заряда":
        st.subheader("Расчёт напряжённости электрического поля")
        q = st.number_input("Заряд q (Кл)", value=1e-6, format="%.2e")
        r = st.number_input("Расстояние r (м)", value=0.1)
        
        if st.button("Рассчитать", key="field"):
            k = 9e9
            E = k * abs(q) / (r ** 2)
            st.success("### Решение:")
            st.latex(r"E = k \cdot \frac{|q|}{r^2}")
            st.write(f"**Дано:** q = {q} Кл, r = {r} м")
            st.info(f"**Ответ:** E = {E:.4g} В/м")
    
    elif task == "Потенциал электрического поля":
        st.subheader("Расчёт потенциала электрического поля")
        q = st.number_input("Заряд q (Кл)", value=1e-6, format="%.2e")
        r = st.number_input("Расстояние r (м)", value=0.1)
        
        if st.button("Рассчитать", key="potential"):
            k = 9e9
            phi = k * q / r
            st.success("### Решение:")
            st.latex(r"\varphi = k \cdot \frac{q}{r}")
            st.write(f"**Дано:** q = {q} Кл, r = {r} м")
            st.info(f"**Ответ:** φ = {phi:.4g} В")
    
    elif task == "Работа электрического поля":
        st.subheader("Расчёт работы электрического поля")
        q = st.number_input("Заряд q (Кл)", value=1e-6, format="%.2e")
        U = st.number_input("Напряжение U (В)", value=100.0)
        
        if st.button("Рассчитать", key="work"):
            A = q * U
            st.success("### Решение:")
            st.latex(r"A = q \cdot U")
            st.write(f"**Дано:** q = {q} Кл, U = {U} В")
            st.info(f"**Ответ:** A = {A:.4g} Дж")
    
    elif task == "Ёмкость плоского конденсатора":
        st.subheader("Ёмкость плоского конденсатора")
        eps = st.number_input("Диэлектрическая проницаемость ε", value=1.0)
        S = st.number_input("Площадь пластин S (м²)", value=0.01, format="%.2e")
        d = st.number_input("Расстояние d (м)", value=0.001)
        
        if st.button("Рассчитать", key="capacitance"):
            eps0 = 8.85e-12
            C = eps0 * eps * S / d
            st.success("### Решение:")
            st.latex(r"C = \varepsilon_0 \cdot \varepsilon \cdot \frac{S}{d}")
            st.write(f"**Дано:** ε = {eps}, S = {S} м², d = {d} м")
            st.info(f"**Ответ:** C = {C:.4g} Ф")
    
    elif task == "Энергия конденсатора":
        st.subheader("Энергия заряженного конденсатора")
        C = st.number_input("Ёмкость C (Ф)", value=1e-6, format="%.2e")
        U = st.number_input("Напряжение U (В)", value=100.0)
        
        if st.button("Рассчитать", key="energy"):
            W = 0.5 * C * (U ** 2)
            st.success("### Решение:")
            st.latex(r"W = \frac{C \cdot U^2}{2}")
            st.write(f"**Дано:** C = {C} Ф, U = {U} В")
            st.info(f"**Ответ:** W = {W:.4g} Дж")
    
    elif task == "Соединение конденсаторов":
        st.subheader("Батарея конденсаторов")
        conn = st.radio("Тип соединения", ["Последовательное", "Параллельное"])
        C1 = st.number_input("Ёмкость C1 (Ф)", value=1e-6, format="%.2e")
        C2 = st.number_input("Ёмкость C2 (Ф)", value=2e-6, format="%.2e")
        
        if st.button("Рассчитать", key="combo"):
            if conn == "Последовательное":
                C_total = (C1 * C2) / (C1 + C2)
                formula = r"\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2}"
            else:
                C_total = C1 + C2
                formula = r"C = C_1 + C_2"
            st.success("### Решение:")
            st.latex(formula)
            st.info(f"**Ответ:** C = {C_total:.4g} Ф")
    
    elif task == "Напряжённость между пластинами":
        st.subheader("Однородное поле между пластинами")
        U = st.number_input("Напряжение U (В)", value=100.0)
        d = st.number_input("Расстояние d (м)", value=0.01)
        
        if st.button("Рассчитать", key="plate"):
            E = U / d
            st.success("### Решение:")
            st.latex(r"E = \frac{U}{d}")
            st.write(f"**Дано:** U = {U} В, d = {d} м")
            st.info(f"**Ответ:** E = {E:.4g} В/м")

# =============================================================================
# МОДУЛЬ 2: ПОСТОЯННЫЙ ТОК (8 задач)
# =============================================================================
def module_dc_current():
    st.header("🔋 Постоянный ток")
    
    task = st.selectbox(
        "Выберите задачу:",
        [
            "Закон Ома (участок цепи)",
            "Закон Ома (полная цепь)",
            "Сопротивление проводника",
            "Мощность электрического тока",
            "Работа электрического тока",
            "Закон Джоуля-Ленца",
            "КПД источника тока",
            "Сила тока через заряд"
        ]
    )
    
    if task == "Закон Ома (участок цепи)":
        st.subheader("Расчёт силы тока на участке цепи")
        U = st.number_input("Напряжение U (В)", value=12.0)
        R = st.number_input("Сопротивление R (Ом)", value=10.0)
        
        if st.button("Рассчитать", key="ohm1"):
            I = U / R
            st.success("### Решение:")
            st.latex(r"I = \frac{U}{R}")
            st.info(f"**Ответ:** I = {I:.4g} А")
    
    elif task == "Закон Ома (полная цепь)":
        st.subheader("Расчёт силы тока в полной цепи")
        eps = st.number_input("ЭДС ε (В)", value=12.0)
        R = st.number_input("Внешнее сопротивление R (Ом)", value=10.0)
        r = st.number_input("Внутреннее сопротивление r (Ом)", value=1.0)
        
        if st.button("Рассчитать", key="ohm2"):
            I = eps / (R + r)
            st.success("### Решение:")
            st.latex(r"I = \frac{\varepsilon}{R + r}")
            st.info(f"**Ответ:** I = {I:.4g} А")
    
    elif task == "Сопротивление проводника":
        st.subheader("Расчёт сопротивления проводника")
        rho = st.number_input("Удельное сопротивление ρ (Ом·м)", value=1.7e-8, format="%.2e")
        l = st.number_input("Длина l (м)", value=1.0)
        S = st.number_input("Площадь сечения S (м²)", value=1e-6, format="%.2e")
        
        if st.button("Рассчитать", key="resistance"):
            R = rho * l / S
            st.success("### Решение:")
            st.latex(r"R = \rho \cdot \frac{l}{S}")
            st.info(f"**Ответ:** R = {R:.4g} Ом")
    
    elif task == "Мощность электрического тока":
        st.subheader("Расчёт мощности тока")
        I = st.number_input("Сила тока I (А)", value=2.0)
        U = st.number_input("Напряжение U (В)", value=12.0)
        
        if st.button("Рассчитать", key="power"):
            P = I * U
            st.success("### Решение:")
            st.latex(r"P = I \cdot U")
            st.info(f"**Ответ:** P = {P:.4g} Вт")
    
    elif task == "Работа электрического тока":
        st.subheader("Расчёт работы тока")
        I = st.number_input("Сила тока I (А)", value=2.0)
        U = st.number_input("Напряжение U (В)", value=12.0)
        t = st.number_input("Время t (с)", value=10.0)
        
        if st.button("Рассчитать", key="work_current"):
            A = I * U * t
            st.success("### Решение:")
            st.latex(r"A = I \cdot U \cdot t")
            st.info(f"**Ответ:** A = {A:.4g} Дж")
    
    elif task == "Закон Джоуля-Ленца":
        st.subheader("Количество теплоты в проводнике")
        I = st.number_input("Сила тока I (А)", value=2.0)
        R = st.number_input("Сопротивление R (Ом)", value=10.0)
        t = st.number_input("Время t (с)", value=10.0)
        
        if st.button("Рассчитать", key="joule"):
            Q = (I ** 2) * R * t
            st.success("### Решение:")
            st.latex(r"Q = I^2 \cdot R \cdot t")
            st.info(f"**Ответ:** Q = {Q:.4g} Дж")
    
    elif task == "КПД источника тока":
        st.subheader("Расчёт КПД источника")
        R = st.number_input("Внешнее сопротивление R (Ом)", value=10.0)
        r = st.number_input("Внутреннее сопротивление r (Ом)", value=1.0)
        
        if st.button("Рассчитать", key="efficiency"):
            eta = R / (R + r) * 100
            st.success("### Решение:")
            st.latex(r"\eta = \frac{R}{R + r} \cdot 100\%")
            st.info(f"**Ответ:** η = {eta:.2f} %")
    
    elif task == "Сила тока через заряд":
        st.subheader("Расчёт силы тока через заряд и время")
        q = st.number_input("Заряд q (Кл)", value=10.0)
        t = st.number_input("Время t (с)", value=5.0)
        
        if st.button("Рассчитать", key="current_charge"):
            I = q / t
            st.success("### Решение:")
            st.latex(r"I = \frac{q}{t}")
            st.info(f"**Ответ:** I = {I:.4g} А")

# =============================================================================
# МОДУЛЬ 3: МАГНЕТИЗМ (7 задач)
# =============================================================================
def module_magnetism():
    st.header("🧲 Магнетизм")
    
    task = st.selectbox(
        "Выберите задачу:",
        [
            "Сила Ампера",
            "Сила Лоренца",
            "Магнитный поток",
            "Радиус движения заряда в поле",
            "Период обращения заряда",
            "Индукция поля прямого провода",
            "Энергия магнитного поля проводника"
        ]
    )
    
    if task == "Сила Ампера":
        st.subheader("Расчёт силы Ампера")
        I = st.number_input("Сила тока I (А)", value=2.0)
        B = st.number_input("Индукция B (Тл)", value=0.1, format="%.2e")
        l = st.number_input("Длина проводника l (м)", value=0.5)
        alpha = st.number_input("Угол α (градусы)", value=90.0)
        
        if st.button("Рассчитать", key="ampere"):
            F = I * B * l * math.sin(math.radians(alpha))
            st.success("### Решение:")
            st.latex(r"F = I \cdot B \cdot l \cdot \sin\alpha")
            st.info(f"**Ответ:** F = {F:.4g} Н")
    
    elif task == "Сила Лоренца":
        st.subheader("Расчёт силы Лоренца")
        q = st.number_input("Заряд q (Кл)", value=1.6e-19, format="%.2e")
        v = st.number_input("Скорость v (м/с)", value=1e6, format="%.2e")
        B = st.number_input("Индукция B (Тл)", value=0.1, format="%.2e")
        alpha = st.number_input("Угол α (градусы)", value=90.0)
        
        if st.button("Рассчитать", key="lorentz"):
            F = abs(q) * v * B * math.sin(math.radians(alpha))
            st.success("### Решение:")
            st.latex(r"F = |q| \cdot v \cdot B \cdot \sin\alpha")
            st.info(f"**Ответ:** F = {F:.4g} Н")
    
    elif task == "Магнитный поток":
        st.subheader("Расчёт магнитного потока")
        B = st.number_input("Индукция B (Тл)", value=0.1, format="%.2e")
        S = st.number_input("Площадь S (м²)", value=0.01, format="%.2e")
        alpha = st.number_input("Угол α (градусы)", value=0.0)
        
        if st.button("Рассчитать", key="flux"):
            Phi = B * S * math.cos(math.radians(alpha))
            st.success("### Решение:")
            st.latex(r"\Phi = B \cdot S \cdot \cos\alpha")
            st.info(f"**Ответ:** Φ = {Phi:.4g} Вб")
    
    elif task == "Радиус движения заряда в поле":
        st.subheader("Радиус траектории заряженной частицы")
        m = st.number_input("Масса m (кг)", value=9.1e-31, format="%.2e")
        v = st.number_input("Скорость v (м/с)", value=1e6, format="%.2e")
        q = st.number_input("Заряд q (Кл)", value=1.6e-19, format="%.2e")
        B = st.number_input("Индукция B (Тл)", value=0.1, format="%.2e")
        
        if st.button("Рассчитать", key="radius"):
            r = m * v / (abs(q) * B)
            st.success("### Решение:")
            st.latex(r"r = \frac{m \cdot v}{|q| \cdot B}")
            st.info(f"**Ответ:** r = {r:.4g} м")
    
    elif task == "Период обращения заряда":
        st.subheader("Период обращения частицы в поле")
        m = st.number_input("Масса m (кг)", value=9.1e-31, format="%.2e")
        q = st.number_input("Заряд q (Кл)", value=1.6e-19, format="%.2e")
        B = st.number_input("Индукция B (Тл)", value=0.1, format="%.2e")
        
        if st.button("Рассчитать", key="period"):
            T = 2 * math.pi * m / (abs(q) * B)
            st.success("### Решение:")
            st.latex(r"T = \frac{2\pi m}{|q| \cdot B}")
            st.info(f"**Ответ:** T = {T:.4g} с")
    
    elif task == "Индукция поля прямого провода":
        st.subheader("Индукция поля прямого проводника с током")
        I = st.number_input("Сила тока I (А)", value=2.0)
        r = st.number_input("Расстояние r (м)", value=0.05)
        
        if st.button("Рассчитать", key="wire"):
            mu0 = 4 * math.pi * 1e-7
            B = mu0 * I / (2 * math.pi * r)
            st.success("### Решение:")
            st.latex(r"B = \frac{\mu_0 \cdot I}{2\pi r}")
            st.info(f"**Ответ:** B = {B:.4g} Тл")
    
    elif task == "Энергия магнитного поля проводника":
        st.subheader("Энергия магнитного поля")
        L = st.number_input("Индуктивность L (Гн)", value=0.1, format="%.2e")
        I = st.number_input("Сила тока I (А)", value=2.0)
        
        if st.button("Рассчитать", key="mag_energy"):
            W = 0.5 * L * (I ** 2)
            st.success("### Решение:")
            st.latex(r"W = \frac{L \cdot I^2}{2}")
            st.info(f"**Ответ:** W = {W:.4g} Дж")

# =============================================================================
# МОДУЛЬ 4: ЭЛЕКТРОМАГНИТНАЯ ИНДУКЦИЯ (7 задач)
# =============================================================================
def module_emi():
    st.header("🔄 Электромагнитная индукция")
    
    task = st.selectbox(
        "Выберите задачу:",
        [
            "ЭДС индукции (Закон Фарадея)",
            "ЭДС самоиндукции",
            "Энергия магнитного поля катушки",
            "Индуктивность через поток",
            "Период колебательного контура",
            "Частота колебательного контура",
            "Трансформатор (коэффициент)"
        ]
    )
    
    if task == "ЭДС индукции (Закон Фарадея)":
        st.subheader("Расчёт ЭДС электромагнитной индукции")
        dPhi = st.number_input("Изменение потока ΔΦ (Вб)", value=0.01, format="%.2e")
        dt = st.number_input("Время Δt (с)", value=0.1)
        
        if st.button("Рассчитать", key="faraday"):
            eps = abs(dPhi / dt)
            st.success("### Решение:")
            st.latex(r"|\varepsilon| = \left|\frac{\Delta\Phi}{\Delta t}\right|")
            st.info(f"**Ответ:** |ε| = {eps:.4g} В")
    
    elif task == "ЭДС самоиндукции":
        st.subheader("Расчёт ЭДС самоиндукции")
        L = st.number_input("Индуктивность L (Гн)", value=0.1, format="%.2e")
        dI = st.number_input("Изменение тока ΔI (А)", value=2.0)
        dt = st.number_input("Время Δt (с)", value=0.1)
        
        if st.button("Рассчитать", key="self_ind"):
            eps = abs(L * dI / dt)
            st.success("### Решение:")
            st.latex(r"\varepsilon_s = \left|L \cdot \frac{\Delta I}{\Delta t}\right|")
            st.info(f"**Ответ:** εₛ = {eps:.4g} В")
    
    elif task == "Энергия магнитного поля катушки":
        st.subheader("Энергия магнитного поля катушки")
        L = st.number_input("Индуктивность L (Гн)", value=0.1, format="%.2e")
        I = st.number_input("Сила тока I (А)", value=2.0)
        
        if st.button("Рассчитать", key="coil_energy"):
            W = 0.5 * L * (I ** 2)
            st.success("### Решение:")
            st.latex(r"W = \frac{L \cdot I^2}{2}")
            st.info(f"**Ответ:** W = {W:.4g} Дж")
    
    elif task == "Индуктивность через поток":
        st.subheader("Расчёт индуктивности через магнитный поток")
        Phi = st.number_input("Магнитный поток Φ (Вб)", value=0.01, format="%.2e")
        I = st.number_input("Сила тока I (А)", value=2.0)
        
        if st.button("Рассчитать", key="inductance"):
            L = Phi / I
            st.success("### Решение:")
            st.latex(r"L = \frac{\Phi}{I}")
            st.info(f"**Ответ:** L = {L:.4g} Гн")
    
    elif task == "Период колебательного контура":
        st.subheader("Период электромагнитных колебаний")
        L = st.number_input("Индуктивность L (Гн)", value=0.1, format="%.2e")
        C = st.number_input("Ёмкость C (Ф)", value=1e-6, format="%.2e")
        
        if st.button("Рассчитать", key="osc_period"):
            T = 2 * math.pi * math.sqrt(L * C)
            st.success("### Решение:")
            st.latex(r"T = 2\pi \sqrt{L \cdot C}")
            st.info(f"**Ответ:** T = {T:.4g} с")
    
    elif task == "Частота колебательного контура":
        st.subheader("Частота электромагнитных колебаний")
        L = st.number_input("Индуктивность L (Гн)", value=0.1, format="%.2e")
        C = st.number_input("Ёмкость C (Ф)", value=1e-6, format="%.2e")
        
        if st.button("Рассчитать", key="osc_freq"):
            nu = 1 / (2 * math.pi * math.sqrt(L * C))
            st.success("### Решение:")
            st.latex(r"\nu = \frac{1}{2\pi \sqrt{L \cdot C}}")
            st.info(f"**Ответ:** ν = {nu:.4g} Гц")
    
    elif task == "Трансформатор (коэффициент)":
        st.subheader("Коэффициент трансформации")
        U1 = st.number_input("Напряжение первичной обмотки U₁ (В)", value=220.0)
        U2 = st.number_input("Напряжение вторичной обмотки U₂ (В)", value=12.0)
        
        if st.button("Рассчитать", key="transformer"):
            k = U1 / U2
            st.success("### Решение:")
            st.latex(r"k = \frac{U_1}{U_2}")
            st.info(f"**Ответ:** k = {k:.2f}")

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