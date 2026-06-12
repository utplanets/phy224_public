NOTEBOOKS_DIR := .notebooks
ZIP_TARGET    := episodes/files/notebooks.zip

QMD_FILES := \
    episodes/basics.qmd \
    episodes/built-in-functions-and-help.qmd \
    episodes/conditionals.qmd \
    episodes/data-types-and-conversion.qmd \
    episodes/fitting-data-to-models.qmd \
    episodes/for-loops.qmd \
    episodes/getting-help.qmd \
    episodes/libraries.qmd \
    episodes/lists.qmd \
    episodes/looping-over-data-sets.qmd \
    episodes/numpy-and-scipy.qmd \
    episodes/optional-fsolve.qmd \
    episodes/optional-newton.qmd \
    episodes/optional-pandas.qmd \
    episodes/optional-pathlib.qmd \
    episodes/optional-sigfigs.qmd \
    episodes/plotting.qmd \
    episodes/programming-style.qmd \
    episodes/reading-tabular-data.qmd \
    episodes/running-and-quitting.qmd \
    episodes/variable-scope.qmd \
    episodes/variables-and-assignment.qmd \
    episodes/wrap-up.qmd \
    episodes/writing-functions.qmd

IPYNB_FILES := $(patsubst episodes/%.qmd,$(NOTEBOOKS_DIR)/%.ipynb,$(QMD_FILES))

.PHONY: all notebooks clean

all: $(ZIP_TARGET)

$(ZIP_TARGET): $(IPYNB_FILES)
	zip -j $@ $^

$(NOTEBOOKS_DIR)/%.ipynb: episodes/%.qmd fix_callouts.py | $(NOTEBOOKS_DIR)
	quarto convert $< --output $@
	python3 fix_callouts.py $@

$(NOTEBOOKS_DIR):
	mkdir -p $@

clean:
	rm -rf $(NOTEBOOKS_DIR) $(ZIP_TARGET)
