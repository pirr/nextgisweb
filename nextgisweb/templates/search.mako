<%inherit file='base.mako' />

<script>
    require([
        "dojo/parser",
        "dojo/ready",
        "dijit/form/Button"
    ], function (
        parser,
        ready
    ) {
        ready(function() {
            parser.parse();
        });
    });
</script>

<div data-dojo-type="dijit/form/Form">
        <input type="text" name="q" data-dojo-type="dijit/form/TextBox" style="width: 20em;" />
        <button data-dojo-type="dijit/form/Button" type="submit">Поиск</button>
</div>

<table class="pure-table pure-table-horizontal" style="width: 100%">
    <thead>
        <tr>
            <th style="width: 5%">#</th>
            <th style="width: 50%">Наименование</th>
            <th style="width: 25%">Тип</th>
            <th style="width: 20%">Владелец</th>
            <th style="width: 0%">&nbsp;</th>
        </tr>
    </thead>
    %for idx, child in enumerate(resources, start=1):
        <tr>
            <td>${idx}</td>
            <td><a style="display: block" href="${child.permalink(request)}">${child.display_name}</a></td>
            <td>${child.cls_display_name}</td>
            <td>${child.owner_user}</td>
            <td style="white-space: nowrap">
                <a class="dijitIconEdit" style="width: 16px; height: 16px; display: inline-block;" href="${request.route_url('resource.update', id=child.id)}"></a>
                <a class="dijitIconDelete" style="width: 16px; height: 16px; display: inline-block;" href="${request.route_url('resource.delete', id=child.id)}"></a>
            </td>
        </tr>
    %endfor
</table>
