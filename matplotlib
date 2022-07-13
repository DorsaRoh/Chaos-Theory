def plt_show(plt, width, dpi=100):
    bytes = io.BytesIO()
    plt.savefig(bytes, format='png', dpi=dpi)
    if hasattr(plt, "close"):
        plt.close()
    bytes.seek(0)
    base64_string = "data:image/png;base64," + \
        base64.b64encode(bytes.getvalue()).decode("utf-8")
    return "<img src='" + base64_string + "' width='" + str(width) + "'>"
