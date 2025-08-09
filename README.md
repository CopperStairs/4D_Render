# Tesseract

**4D hypercube render**

---

*To rotate 4D hypercube use Q, W, E, R, T, Y, A, S, D, F, G, H keys*

*Q, W* - rotate around the axis *xw*

*E, R* - rotate around the axis *yw*

*T, Y* - rotate around the axis *zw*

*A, S* - rotate around the axis *xy*

*D, F* - rotate around the axis *xz*

*G, H* - rotate around the axis *yz*



```mermaind
flowchart TD
    line_segment["Line segment (1D cube) has 2 1D sides"]
    square["Square (2D cube) has 4 1D sides"]
    cube["Cube (3D cube) has 6 2D sides"]
    tesseract["Tesseract (4d hypercube) has 8 3D sides"]
    line_segment --> square --> cube --> tesseract
```