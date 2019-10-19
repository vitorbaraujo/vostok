DIST_DIR=dist
PYTHON_EXEC=python3

generate: clean
	@$(PYTHON_EXEC) setup.py sdist bdist_wheel	

upload:
	@$(PYTHON_EXEC) -m twine upload $(DIST_DIR)/*

test-upload:
	@$(PYTHON_EXEC) -m twine upload --repository-url https://test.pypi.org/legacy/ $(DIST_DIR)/*

run-test:
	@$(PYTHON_EXEC) vostok/test/example.py vostok/test/test_data/sample.md

clean:
	@rm -rf $(DIST_DIR) 
