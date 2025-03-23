from contextlib import contextmanager
import plotly.graph_objects as go
import plotly.io as pio
import seaborn as sns
import time


from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def table_style():
    return TableStyle(
        [
            # En-tête de la table avec fond vert pomme et texte blanc
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkgreen),  # Vert pomme
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            # Corps de la table avec fond blanc
            (
                "BACKGROUND",
                (0, 1),
                (-1, -1),
                colors.white,
            ),  # Fond blanc pour les cellules
            # Bordure des cellules
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]
    )


def style_plotly():
    return go.layout.Template(
        layout=dict(
            paper_bgcolor="white",  # Fond du graphique en blanc
            plot_bgcolor="white",  # Fond de la zone de traçage en blanc
            font=dict(color="black", family="Arial"),  # Couleur et style de la police
            xaxis=dict(
                showgrid=True,  # Afficher la grille
                gridcolor="lightgrey",  # Couleur de la grille légère
                zeroline=False,  # Ligne zéro masquée
                showline=True,  # Afficher la ligne de l'axe
                linecolor="green",  # Ligne de l'axe en vert
            ),
            yaxis=dict(
                showgrid=True,  # Afficher la grille
                gridcolor="lightgrey",  # Couleur de la grille légère
                zeroline=False,  # Ligne zéro masquée
                showline=True,  # Afficher la ligne de l'axe
                linecolor="green",  # Ligne de l'axe en vert
            ),
            colorway=[
                "#03A64A",
                "#025940",
                "#026873",
                "#024059",
                "#04BF8A",
            ],  # Palette de couleurs pour les tracés
            title=dict(
                font=dict(size=20, color="darkgreen", weight="bold", family="Arial"),
                x=0.2,  # Centrage du titre
            ),
        )
    )


def style_seaborn():
    # Définir les paramètres du thème de Seaborn
    sns.set_theme(
        style="whitegrid",  # Fond blanc avec grille
        palette=[
            "#03A64A",
            "#025940",
            "#026873",
            "#024059",
            "#04BF8A",
        ],  # Palette de couleurs pour les tracés
        rc={
            "axes.facecolor": "white",  # Fond de la zone de traçage en blanc
            "axes.edgecolor": "green",  # Couleur de la ligne de l'axe
            "axes.grid": True,  # Afficher la grille
            "grid.color": "lightgrey",  # Couleur de la grille
            "grid.linestyle": "-",  # Style de la grille (ligne continue)
            "xtick.color": "black",  # Couleur des ticks sur l'axe x
            "ytick.color": "black",  # Couleur des ticks sur l'axe y
            "axes.labelcolor": "black",  # Couleur des labels des axes
            "text.color": "darkgreen",  # Couleur du texte global (titre compris)
            "axes.titlesize": 20,  # Taille du texte du titre
            "axes.titlelocation": "left",  # Positionnement du titre (centrage gauche)
            "axes.titleweight": "bold",  # Titre en gras
            "axes.titlepad": 20,  # Espacement du titre
            # "axes.titleposition": "center",  # Centrage du titre
            "figure.facecolor": "white",  # Fond de la figure en blanc
            "lines.linewidth": 1,  # Épaisseur des lignes
        },
    )


def conv_df_to_table(df, style):
    table_data = [df.columns.values.tolist()] + df.values.tolist()
    table = Table(table_data)
    table.setStyle(style)
    return table


def style_title_left(styles):
    return ParagraphStyle(
        name="LeftAlignedTitle",
        parent=styles["Title"],
        alignment=0,  # 0 pour alignement à gauche
    )


CustomStyle = {
    # Créer un style personnalisé pour le titre
    "custom_title_style": ParagraphStyle(
        name="CustomTitle",
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=30,
        spaceAfter=12,
        alignment=1,  # Center align
        textColor="darkgreen",
    ),
    # Créer un style personnalisé pour le texte du corps
    "custom_body_style": ParagraphStyle(
        name="CustomBody",
        fontName="Helvetica",
        fontSize=12,
        leading=14,
        spaceBefore=6,
        spaceAfter=6,
        alignment=0,  # Left align
        textColor="black",
    ),
}


@contextmanager
def pdf(file_name):
    # At start
    doc = SimpleDocTemplate(file_name + ".pdf", pagesize=letter)

    elements = []
    styles = getSampleStyleSheet()
    left_aligned_title = style_title_left(styles)

    styles = CustomStyle

    try:
        # Passer la liste elements et les styles au bloc withr
        yield elements, styles, left_aligned_title

    finally:
        # À la fin, construire le PDF
        doc.build(elements)
        print("-" * 100 + f"\nPDF created.\n" + "-" * 100)


if __name__ == "__main__":
    with pdf() as (elements, styles):
        time.sleep(1)
