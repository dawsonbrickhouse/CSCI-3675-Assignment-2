# CSCI-3675-Assignment-2

Constrained SQL generation with Outlines, Lark and Qwen2.5-Coder-1.5B-Instruct.

| File | Contents |
| --- | --- |
| `assignment2_constrained_sql.ipynb` | The submission: grammar and parse tests, both generation paths, prompts, validity table, constrained Group 2 results, discussion. Saved with the outputs of the run the discussion refers to. |
| `a2.db` | The posted SQLite database (the notebook rebuilds it if it is missing). |
| `seed_a2.py` | The posted script that builds `a2.db`. |

## Running

On Colab, upload the notebook (and optionally `a2.db`) and run all cells. The first cell pins Outlines,
llguidance, Lark, Transformers and Accelerate.

Locally:

```bash
python -m venv a2env && source a2env/bin/activate
pip install torch            # use the pytorch.org selector for CUDA builds
pip install "outlines==1.3.3" "llguidance==1.9.1" "lark==1.3.1" "transformers==5.18.0" "accelerate==1.15.0" pandas jupyter
jupyter nbconvert --to notebook --execute --inplace assignment2_constrained_sql.ipynb
```
