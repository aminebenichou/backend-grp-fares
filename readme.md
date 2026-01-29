<form action="" method="post">
        {% csrf_token %}
        <input type="text" name="title" id="title" value="{{note.title}}">
        <input type="text" name="content" id="content" value="{{note.content}}">
        <input type="submit" value="Save">
</form>

FORMDATA
{
    'title':'djakjasdn',
    'content':'djakjasdn'
}