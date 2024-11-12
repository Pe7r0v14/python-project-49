install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --break-system-packages --force-reinstall

add:
	git add --all
commit:
	git commit --all
push:
	git push --all
