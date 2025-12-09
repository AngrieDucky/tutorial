from quart import Blueprint, abort, render_template, request, jsonify, send_from_directory, redirect

blueprint = Blueprint('oleg', __name__, template_folder="templates")

@blueprint.route('/', methods=["GET", "POST"])
async def main_page():
    ctx: dict = {"title": "Главная"}
    print(blueprint.template_folder)
    return await render_template("index.html", context=ctx)