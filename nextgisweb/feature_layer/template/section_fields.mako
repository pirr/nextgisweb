<table class="pure-table pure-table-horizontal" style="width: 100%">
    <thead><tr>
        <th>Ключ</th>
        <th>Тип</th>
        <th>Наименование</th>
        <th style="width: 0; text-align: center;">Таб.</th>
    </tr></thead>
    %for idx, field in enumerate(obj.fields):
        <tr class="${'pure-table-odd' if idx % 2 else 'pure-table-even'}" style="${'text-decoration: underline;' if field.id == obj.feature_label_field_id else '' | n}">
            <td>${field.keyname}</td>
            <td>${field.datatype}</td>
            <td>${field.display_name}</td>
            <td style="text-align: center;">${u"Да" if field.grid_visibility else u"Нет" | n}</td>
        </tr>
    %endfor
</table>