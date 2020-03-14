# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, render_template, request, flash, redirect
from contact_model import Contact

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True


@app.route(r'/', methods=['GET'])
def contact_book():
    # contacts = Contact.query().fetch()
    # return render_template('contact_book.html', contacts=contacts)
    return render_template('contact_book.html')


@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
    if request.form:
        contact = Contact(name=request.form.get('name'),
                          phone=request.form.get('phone'),
                          email=request.form.get('email'))

        contact.put()
        flash('¡Se añadió el contacto!')

    return render_template('add_contact.html')


@app.route(r'/contacts/<uid>', methods=['GET'])
def contact_details(uid):
    contact = Contact.get_by_id(int(uid))

    if not contact:
        return redirect('/', code=301)

    return render_template('contact.html', contact=contact)


@app.route(r'/delete', methods=['POST'])
def delete_contact():
    contact = Contact.get_by_id(int(request.form.get('uid')))
    contact.key.delete()
    return redirect('/contacts/{}'.format(contact.key.id()))


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
