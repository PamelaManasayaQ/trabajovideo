from manim import *

class OptimizacionRobot(Scene):
    def construct(self):
        # Títulos y etiquetas
        titulo = Text("Maximización de Producción con Restricciones").to_edge(UP)
        self.play(Write(titulo))

        # Sistema de ejes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 12, 2],
            axis_config={"include_numbers": True}
        )

        x_label = axes.get_x_axis_label(Tex("Horas Robot A"))
        y_label = axes.get_y_axis_label(Tex("Horas Robot B"))
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Restricciones como líneas
        # Restricción 20x + 30y <= 500 -> y <= (500 - 20x)/30
        linea_energia = axes.plot(lambda x: (500 - 20*x) / 30, x_range=[0, 10], color=BLUE)
        restriccion_energia = MathTex("20x + 30y \leq 500").next_to(linea_energia, UP)

        # Restricción x <= 8 (Robot A puede operar un máximo de 8 horas)
        restriccion_x8 = DashedLine(axes.coords_to_point(8, 0), axes.coords_to_point(8, 12), color=RED)
        restriccion_x8_label = MathTex("x \\leq 8").next_to(restriccion_x8, RIGHT)

        # Restricción y <= 6 (Robot B puede operar un máximo de 6 horas)
        restriccion_y6 = DashedLine(axes.coords_to_point(0, 6), axes.coords_to_point(10, 6), color=GREEN)
        restriccion_y6_label = MathTex("y \\leq 6").next_to(restriccion_y6, LEFT)

        # Animaciones de las restricciones
        self.play(Create(linea_energia), Write(restriccion_energia))
        self.play(Create(restriccion_x8), Write(restriccion_x8_label))
        self.play(Create(restriccion_y6), Write(restriccion_y6_label))

        # Rellenar la región factible
        region_factible = Polygon(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(8, 0),
            axes.coords_to_point(8, (500 - 20 * 8) / 30),
            axes.coords_to_point(6, 6),
            axes.coords_to_point(0, 6),
            color=YELLOW,
            fill_opacity=0.5
        )

        self.play(FadeIn(region_factible))

        # Solución óptima
        solucion_optima = Dot(axes.coords_to_point(8, 4), color=RED)
        solucion_label = MathTex("(8, 4)").next_to(solucion_optima, UR)

        self.play(FadeIn(solucion_optima), Write(solucion_label))

        # Mostrar la solución óptima en la gráfica
        produccion_max = Text("Máx Producción: 540 piezas", color=RED).next_to(titulo, DOWN)
        self.play(Write(produccion_max))

        # Mantener la animación visible por un tiempo
        self.wait(3)
