This project simulates a cloud-hosted e-commerce environment using local VM/WSL.


- VM setup instructions (infra/)
- Simple web server (web/index.html)
- Dataset and cleaning (data/, scripts/data_cleaning.py)
- Visualizations (scripts/plot_example.py)
- Encryption demo (scripts/encryption_demo.py)


1. Follow infra/setup_vm_instructions.txt to prepare a VM or WSL.
2. Run `scripts/setup_venv.sh` to create venv and install libs.
3. Activate venv, then:
   - `python3 scripts/data_cleaning.py`
   - `python3 scripts/plot_example.py`
   - `python3 scripts/encryption_demo.py`
