from flask import Flask, redirect, url_for, render_template, send_file
app = Flask(__name__)
app.config.from_object('config')
planer_data = {
  'overview' : {'name': 'Overview', 'info': 'A digital planner is a tool that helps individuals organize their schedules and tasks in a digital format. It offers customization options, flexibility, and the ability to access and update schedules from anywhere. Digital planners are ideal for boosting productivity and staying organized.'},
  'to-do-lists' : {'name': 'To-Do Lists', 'info': 'Here are some ideas for To-Do Lists: To-do lists are lists of tasks that people can use to organize their work. There are different types of to-do lists, such as ones that list tasks by priority, or ones that group tasks by project. To use them effectively, people should prioritize tasks by importance, set realistic deadlines, and break down big tasks into smaller ones. By doing this, people can stay on top of their work and avoid feeling overwhelmed.'},
  'calendar' : {'name': 'Calendar', 'info': 'Here we will add a new calendar feature where you can track your plans in a visual calendar format. This feature will be added later on.'},
  'visionboards' : {'name': 'Visionboards', 'info': 'Here you can add visionboards of all kinds. Some Ideas: Vision boards are a visual representation of an individuals goals, dreams, and aspirations. They are typically created by collecting and arranging images, quotes, and other visual cues that represent the things that the individual wants to achieve, have, or become. The idea is that by focusing on these images, the individual can create a positive mindset and manifest their desired outcomes. Vision boards can be physical, made on a cork board or poster, or digital, created on a computer or mobile device. They can be used to help individuals stay motivated and inspired, and serve as a reminder of their goals and aspirations.'},
  'recipe-collection' : {'name': 'Recipe Collection', 'info': 'Your recipes all in one place. Once this section is more developed you can also add pictures.'},
}
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/about')
def about():
  return 'This is a digital planer.'
@app.route('/about-me')
def about_me():
  return redirect(url_for('about'))
@app.route('/planer')
def planer():
    planer_data
    return render_template('planer.html', planer=planer_data)
@app.route('/planer/<slug>')
def cookie(slug):
  if slug in planer_data:
    return '<h1>' + planer_data[slug]['name'] + '</h1>' + '<p>' + planer_data[slug]['info'] + '</p>'
  else:
    return 'Sorry we could not find that info.' 
@app.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment=True)
if __name__ == '__main__':
    app.run()   