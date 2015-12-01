default:

.PHONY: notebooks
notebooks:
	sh scripts/run-all-notebooks.sh

data/H-2A-experience-requirements.csv: scripts/get-lcr-experience-data.py
	python $< overall > $@

data/H-2A-experience-requirements-by-state.csv: scripts/get-lcr-experience-data.py
	python $< by_state > $@
