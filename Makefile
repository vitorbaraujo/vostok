DIST_DIR=dist
PYTHON_EXEC=python3

generate: clean
	@$(PYTHON_EXEC) setup.py sdist bdist_wheel	

upload:
	@$(PYTHON_EXEC) -m twine upload $(DIST_DIR)/*

test-upload:
	@$(PYTHON_EXEC) -m twine upload --repository-url https://test.pypi.org/legacy/ $(DIST_DIR)/*

clean:
	@rm -rf $(DIST_DIR) 
