from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib


def create_formula(formula="", font_size=16, dpi=100, format_="png", path=""):
    matplotlib.rcParams["mathtext.fontset"] = "stix"
    matplotlib.rcParams["font.family"] = "STIXGeneral"
    matplotlib.pyplot.title(r"ABC123 vs $\mathrm{ABC123}^{123}$")
    fig = plt.figure(facecolor="#F0F0F0")
    text = fig.text(0, 0, r"{0}".format(formula), fontsize=font_size)
    fig.savefig(BytesIO(), dpi=dpi, facecolor=fig.get_facecolor(), edgecolor="none")
    bbox = text.get_window_extent()
    width, height = bbox.size / float(dpi) + 0.05
    fig.set_size_inches((width, height))
    dy = (bbox.ymin / float(dpi)) / height
    text.set_position((0, -dy))
    buffer_ = BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    buffer_.seek(0)
    with open(path + "." + format_, "wb") as image_file:
        image_file.write(buffer_.getvalue())
