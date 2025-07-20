# -*- coding: utf-8 -*-
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "kiara==0.5.25",
#     "kiara_plugin.core_types==0.5.3",
#     "marimo",
# ]
# ///

# -*- coding: utf-8 -*-

import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
async def _():
    import micropip

    await micropip.install("lzma")
    await micropip.install("kiara")
    await micropip.install("kiara_plugin.core_types")
    return


@app.cell
def _():
    from kiara.api import KiaraAPI
    from kiara_plugin.core_types import find_data_types
    from typing import Union
    import marimo as mo


    kiara = KiaraAPI.instance()
    kiara.set_active_context("core_types", create=True)
    return (kiara,)


@app.cell
def _(kiara):

    for op in kiara.list_operations():
        print(f"- {op}")
    return


@app.cell
def _(kiara):
    job_desc = {
        "operation": "logic.and",
        "inputs": {
            "a": True,
            "b": False
        },
        "comment": "And operation."
    }
    job_result = kiara.run_job(**job_desc)
    job_result["y"].data

    return


if __name__ == "__main__":
    app.run()
