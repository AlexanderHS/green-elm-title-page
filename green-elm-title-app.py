import psutil
from flask import Flask, render_template, request
from config import SERVER_NAME, SERVER_ICON

app = Flask(__name__)

from typing import Dict


def get_disk_usage() -> Dict[str, int]:
    """
    Get disk usage information for the system.
    Returns:
        A dictionary containing total, used, free space (in GB), and usage percentage.
    """
    try:
        disk_usage = (
            psutil.disk_usage("/home")
            if SERVER_NAME != "dark-helm"
            else psutil.disk_usage("/mnt/grove")
        )
    except FileNotFoundError:
        disk_usage = psutil.disk_usage("/")

    gb_factor = 2**30  # 1 GB in bytes

    return {
        "total": int(disk_usage.total // gb_factor),
        "used": int(disk_usage.used // gb_factor),
        "free": int(disk_usage.free // gb_factor),
        "percent": int(disk_usage.percent),
    }


@app.route("/")
def index() -> str:
    """
    Render the index page with disk usage information and server details.

    Returns:
        str: Rendered HTML template as a string.
    """
    disk_usage: Dict[str, int] = get_disk_usage()
    server_name: str = SERVER_NAME
    server_icon: str = SERVER_ICON
    title: str = server_name.replace("-", " ").title()

    return render_template(
        "index.html",
        disk_usage=disk_usage,
        SERVER_NAME=server_name,
        SERVER_ICON=server_icon,
        title=title,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
