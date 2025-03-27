### 1. setup venv base html and app (https://github.com/tonyjustdevs/learning_flask/issues/23)
- [ ] 1. setup venv base html and app (https://github.com/tonyjustdevs/learning_flask/issues/23)
    - [ ] add virtual environment .venv_pet_rego (https://github.com/tonyjustdevs/learning_flask/issues/24)
    - [ ] add app (Flask instance) of __name__ in app.py (https://github.com/tonyjustdevs/learning_flask/issues/25)
    - [ ] add layout.html as base jinja template (https://github.com/tonyjustdevs/learning_flask/issues/26)
    - [ ] add index.html extending layout.html (https://github.com/tonyjustdevs/learning_flask/issues/27)
<hr>

### 2. setup index route (https://github.com/tonyjustdevs/learning_flask/issues/28)
- [ ] 2. setup index route  (https://github.com/tonyjustdevs/learning_flask/issues/28)
    - [ ] add / default route via @app (python decorator) (https://github.com/tonyjustdevs/learning_flask/issues/29)
    - [ ] add GET as an allowed method to / route decorator (https://github.com/tonyjustdevs/learning_flask/issues/30)
    - [ ] add index (python) *decorated* function with render_template (flask) index.html (https://github.com/tonyjustdevs/learning_flask/issues/31)
    - [ ] add form /register route to form action as a post method (https://github.com/tonyjustdevs/learning_flask/issues/32)
    - [ ] add **name** input form text (https://github.com/tonyjustdevs/learning_flask/issues/33)
    - [ ] add sport optionss as a drop-down to input form select (https://github.com/tonyjustdevs/learning_flask/issues/34)
    - [ ] add **sport** as an option with disabled and selected attribute  (https://github.com/tonyjustdevs/learning_flask/issues/35)
<hr>

### 3. setup register route (https://github.com/tonyjustdevs/learning_flask/issues/36)
- [ ] 3. setup register route (https://github.com/tonyjustdevs/learning_flask/issues/36)
    - [ ] add /register route via @app decorator (https://github.com/tonyjustdevs/learning_flask/issues/37)
    - [ ] add POST as an allowed method to /register route decorator (https://github.com/tonyjustdevs/learning_flask/issues/38)
    - [ ] add register (python) *decorated* function with render_template (flask) success.html (https://github.com/tonyjustdevs/learning_flask/issues/39)
    - [ ] add success.html extending layout.html (https://github.com/tonyjustdevs/learning_flask/issues/40)
<hr>

### 4. server side validation v1  (https://github.com/tonyjustdevs/learning_flask/issues/41)
- [ ] 4. server side validation v1 - if-else logic for missing data (https://github.com/tonyjustdevs/learning_flask/issues/41)
    - [ ] add missing data (name or sport) from form.get to render failure.html else success.html (https://github.com/tonyjustdevs/learning_flask/issues/42)
    - [ ] add failure.html (https://github.com/tonyjustdevs/learning_flask/issues/43)
<hr>

### 5. server side validation v2 (https://github.com/tonyjustdevs/learning_flask/issues/44)
- [ ] 5. server side validation v2 - a global SPORTS python list (https://github.com/tonyjustdevs/learning_flask/issues/44)
    - [ ] add SPORTS list of available sports (https://github.com/tonyjustdevs/learning_flask/issues/45)
    - [ ] add sports=SPORTS parameter to "/" default route render_template (https://github.com/tonyjustdevs/learning_flask/issues/46)
    - [ ] add jinja for-loop to generate each sport in sports as select options-values (https://github.com/tonyjustdevs/learning_flask/issues/47)
    - [ ] add not in SPORTS logic to validate input (https://github.com/tonyjustdevs/learning_flask/issues/48)
<hr>

- [ ] Update input to radio sport options on index.html (https://github.com/tonyjustdevs/learning_flask/issues/49)

<hr>

### 6. server side validation v3 (https://github.com/tonyjustdevs/learning_flask/issues/50)
- [ ] 6. server side validation v3 - customised informative error routes (https://github.com/tonyjustdevs/learning_flask/issues/50)
    - [ ] add **missing** name validation - show "Missing Name" jinja argument toerror.html (https://github.com/tonyjustdevs/learning_flask/issues/51)
    - [ ] add **missing** sport validation - show "Missing Sport" jinja argument toerror.html (https://github.com/tonyjustdevs/learning_flask/issues/52)
    - [ ] add **invalid** sport shows "Invalid Sport" jinja argument to error.html (https://github.com/tonyjustdevs/learning_flask/issues/53)
    - [ ] add error.html (https://github.com/tonyjustdevs/learning_flask/issues/54)
    - [ ] add static **image** to error.html (https://github.com/tonyjustdevs/learning_flask/issues/55)
<hr>

### 7. setup registrants route (https://github.com/tonyjustdevs/learning_flask/issues/56)
- [ ] 7. setup registrants route (https://github.com/tonyjustdevs/learning_flask/issues/56)
    - [ ] add REGISTRANTS empty dict in app.py (https://github.com/tonyjustdevs/learning_flask/issues/57)
    - [ ] add [name]=sport key-value to REGISTRANTS dict for each registrant (https://github.com/tonyjustdevs/learning_flask/issues/58)
    - [ ] add /registrant route via @app decorator (https://github.com/tonyjustdevs/learning_flask/issues/59)
    - [ ] add GET as an allowed method to /registrant route decorator (https://github.com/tonyjustdevs/learning_flask/issues/60)
    - [ ] add registrant (python) *decorated* function with render_template (flask) registrant.html (https://github.com/tonyjustdevs/learning_flask/issues/61)
    - [ ] add jinja argument REGISTRANTS dict to render_template registrant.html (https://github.com/tonyjustdevs/learning_flask/issues/62)
<hr>

### 8. setup registrant html page (https://github.com/tonyjustdevs/learning_flask/issues/63)
- [ ] 8. add registrant.html extending layout.html (https://github.com/tonyjustdevs/learning_flask/issues/63)
    - [ ] add jinja for-loop for Name to li tags inside a ul tag (https://github.com/tonyjustdevs/learning_flask/issues/64)
    - [ ] add table html with thead-tr with 2 th Name and Sport (https://github.com/tonyjustdevs/learning_flask/issues/65)
    - [ ] add tbody and jinjak for-loop each tr showing name and sport (https://github.com/tonyjustdevs/learning_flask/issues/66)
<hr>

### 9. set up sqlite sql db (https://github.com/tonyjustdevs/learning_flask/issues/67)
- [ ] 9. add sqlite sql db schemaa (https://github.com/tonyjustdevs/learning_flask/issues/67)
    - [ ] add INSERT INTO to sql-db via db.execute() for name and sport in register route replacing REGISTRANTS dict (https://github.com/tonyjustdevs/learning_flask/issues/68)
    - [ ] add SELECT name and sport sql stmt via db.execute() from sql-db (https://github.com/tonyjustdevs/learning_flask/issues/69)
