# Tesseract

**4D hypercube render**

---

## Controls

*To rotate 4D hypercube use Q, W, E, R, T, Y, A, S, D, F, G, H keys*

-*Q, W* - rotate around the axis *xw*

-*E, R* - rotate around the axis *yw*

-*T, Y* - rotate around the axis *zw*

-*A, S* - rotate around the axis *xy*

-*D, F* - rotate around the axis *xz*

-*G, H* - rotate around the axis *yz*

## How it works (geometry)

![Alt Text](images/image.png)

```mermaid
flowchart TD
    line_segment["Line segment (1D cube) has 2 0D sides and 2 vertexes"]
    square["Square (2D cube) has 4 1D sides and 4 vertexes"]
    cube["Cube (3D cube) has 6 2D sides and 8 vertexes"]
    tesseract["Tesseract (4D hypercube) has 8 3D sides and 16 vertexes"]
    line_segment --> square --> cube --> tesseract
```
