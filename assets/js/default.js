$(document).ready(function() {
    var count = 3;
    var table = $('#incT1').DataTable({
        "ajax": "./data.json",
        "lengthMenu": [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]], 
        scrollY:        200,
        scrollCollapse: true,
        "columns": [
            {
                "orderable":      false,
                "data":           null,
                "defaultContent": ''
            },
            { "data": "name" },
            { "data": "position" },
            { "data": "office" },
            { "data": "salary" }
        ]
    });

    // Add click for row
    $('#incT1 tbody').on('click', 'tr', function () {
        var data = table.row(this).data();
        
        //Open in new tab
        var win = window.open("views/detail.html", '_blank');
        win.focus();
    });

    var table2 = $('#incT2').DataTable({
        "ajax": "./data.json",
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "columns": [
            {
                "className":      'details-control',
                "orderable":      false,
                "data":           null,
                "defaultContent": ''
            },
            { "data": "name" },
            { "data": "position" },
            { "data": "office" },
            { "data": "salary" }
        ],
        "order": [[1, 'asc']]
    });

    // Add click for children elements
     $('#incT2 tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = table2.row(tr);
 
        if (row.child.isShown()) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child(format2("IncT3"+count)).show();
            row.child().addClass('table-child');
            tr.addClass('shown');
            var newTable = $('#IncT3'+count).DataTable({
                "ajax": "assets/data/data.json",
                "lengthMenu": [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]], 
                scrollY:        200,
                scrollCollapse: true,
                "columns": [
                    {
                        "orderable":      false,
                        "data":           null,
                        "defaultContent": ''
                    },
                    { "data": "name" },
                    { "data": "position" },
                    { "data": "office" },
                    { "data": "salary" }
                ]
            });
            count = count + 1;
        }
    });

    function format (d) {
        return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
            '<tr>'+
                '<td>Full name:</td>'+
                '<td>'+d.name+'</td>'+
            '</tr>'+
            '<tr>'+
                '<td>Extension number:</td>'+
                '<td>'+d.extn+'</td>'+
            '</tr>'+
            '<tr>'+
                '<td>Extra info:</td>'+
                '<td>And any further details here (images etc)...</td>'+
            '</tr>'+
        '</table>';
    }

    function format2 (id) {
        return '<table id="' + id + '" class="table table-striped" cellspacing="0" width="100%">' +
            '<thead>'+
                '<tr>'+
                    '<th></th>'+
                    '<th>Name</th>'+
                    '<th>Position</th>'+
                    '<th>Office</th>'+
                    '<th>Salary</th>'+
               ' </tr>'+
            '</thead>'+
        '</table>';
    }

    function t(data, type, row, meta) {
        var cusip = row["CUSIP"];
        
        var generatedNodeText = "<a data-toggle='collapse' data-target='#" + cusip + "'>" + data.length + " Documents</a>";
        generatedNodeText += "<div id='" + cusip + "' class='collapse'>";
        
        // Generate the anchors in the accordion.
        // You will generate whatever content is specific to your situation.
        for (var i in data) { // iterate over the objects in the XBRL array
            generatedNodeText += "<a href='" + "data[i].URL" + "'>" + "data[i].Text "+ "</a><br />";
        }
        
        generatedNodeText += "</div>";
        
        return generatedNodeText;
    }
});