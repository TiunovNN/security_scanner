from flask import render_template, flash, redirect, url_for, request
from flask_babel import _
from flask_login import login_required, current_user

import web.profiles
from web import app, db
from web.models import ScanProfile

ACTIVE = 'profiles'


@app.route('/profiles')
@login_required
def profiles():
    return render_template(
        'profiles/profile_list.html',
        scan_profiles=current_user.scan_profiles,
        active=ACTIVE,
    )


@app.route('/profiles/create', methods=['GET', 'POST'])
@login_required
def create_profile():
    form = web.profiles.forms.ScanProfileForm()

    if not form.validate_on_submit():
        return render_template(
            'profiles/edit_profile.html',
            form=form,
            action=_('Create profile'),
            active=ACTIVE,
        )

    profile = ScanProfile(
        owner_id=current_user.get_id()
    )
    form.populate_obj(profile)
    db.session.add(profile)
    db.session.commit()
    flash(_('Profile was created'))
    return redirect(url_for('profiles'))


@app.route('/profiles/edit/<int:profile_id>', methods=['GET', 'POST'])
@login_required
def edit_profile(profile_id):
    profile = current_user.scan_profiles.filter_by(id=profile_id).first()

    if not profile:
        return redirect(url_for('profiles'))

    form = web.profiles.forms.ScanProfileForm()

    if not form.validate_on_submit():
        form.populate(profile)
        return render_template(
            'profiles/edit_profile.html',
            form=form,
            action=_('Edit profile'),
            active=ACTIVE,
        )

    form.populate_obj(profile)

    db.session.commit()
    flash(_('Profile was edited'))
    return redirect(url_for('profiles'))


@app.route('/profiles/delete', methods=['POST'])
@login_required
def delete_profile():
    profiles = request.form.getlist('profile_ids[]')
    if not profiles:
        return redirect(url_for('profiles'))

    current_user.scan_profiles.filter(
        ScanProfile.id.in_(profiles)
    ).delete(synchronize_session=False)
    db.session.commit()
    return redirect(url_for('profiles'))
