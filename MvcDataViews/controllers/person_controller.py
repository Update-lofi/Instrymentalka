from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.person import Person, PersonForm

person_bp = Blueprint('person', __name__, url_prefix='/person')

# Глобальный список для хранения данных (аналог static List<Person> people)
people = []

@person_bp.route('/')
def index():
    """Отображение списка всех людей"""
    return render_template('person/index.html', people=people)

@person_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Создание нового человека"""
    form = PersonForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            person = Person(
                id=form.id.data,
                name=form.name.data,
                age=form.age.data,
                phone=form.phone.data,
                email=form.email.data
            )
            people.append(person)
            flash('Person created successfully!', 'success')
            return redirect(url_for('person.index'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'{field}: {error}', 'error')
    
    return render_template('person/create.html', form=form)

@person_bp.route('/details/<int:id>')
def details(id):
    """Просмотр деталей человека"""
    person = next((p for p in people if p.id == id), None)
    if person is None:
        flash('Person not found', 'error')
        return redirect(url_for('person.index'))
    return render_template('person/details.html', person=person)

@person_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Редактирование человека"""
    person = next((p for p in people if p.id == id), None)
    if person is None:
        flash('Person not found', 'error')
        return redirect(url_for('person.index'))
    
    form = PersonForm(obj=person)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            person.id = form.id.data
            person.name = form.name.data
            person.age = form.age.data
            person.phone = form.phone.data
            person.email = form.email.data
            flash('Person updated successfully!', 'success')
            return redirect(url_for('person.index'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'{field}: {error}', 'error')
    
    return render_template('person/edit.html', form=form, person=person)

@person_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """Удаление человека"""
    person = next((p for p in people if p.id == id), None)
    if person is None:
        flash('Person not found', 'error')
        return redirect(url_for('person.index'))
    
    if request.method == 'POST':
        people.remove(person)
        flash('Person deleted successfully!', 'success')
        return redirect(url_for('person.index'))
    
    return render_template('person/delete.html', person=person)