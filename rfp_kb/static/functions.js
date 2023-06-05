function Test()
{
  alert ('This is a test function');
  // f = document.forms.frm;
  // f.action = "/test/";
  // f.method = "POST";
  // f.submit();
}

function ProdDelete()
{
  f = document.forms.frm;
  f.action = "/product_delete/";
  f.method = "POST";
  f.submit();
}

function ProdSearch()
{
  f = document.forms.frm;
  f.action = "/prod_search/";
  f.method = "POST";
  f.submit();
}

function ProductSelection(id,name,description,status,type)
{
  f=document.forms.frm;
  f.id.value=id;
  f.prod_name.value=name;
  f.prod_description.value=description;
  f.product_type.value=type;

}

function ProductAdd()
{
  f = document.forms.frm;
  f.action = "/product_add/";
  f.method = "POST";
  f.submit();
}


function MainSearch() 
{
  f = document.forms.frm;
  question = f.elements.txtQuestion.value;
  f.action = "/rfp_qa_list/";
  f.method = "POST";
  f.submit();
}


function Tender()
{
  f = document.forms.frm;
  f.method ="POST";
  f.action="/tender/";
  f.submit();
}
function Product ()
{
  
  f = document.forms.frm;
  f.method ="POST";
  f.action="/prod_view/0";
  f.submit();
}

function MainAdd()
{
  f = document.forms.frm;
  // question = f.elements.txtQuestion.value;
  f.txtProduct_value.value = f.txtProduct.value;
  f.txtRfp_value.value=f.txtRfp.value;
  f.action = "/rfp_addrecord/";
  f.method="POST";
  f.submit();
  
}

function MainUpdate(id)
{

  f = document.forms.frm;
  f.txtProduct_value.value = f.txtProduct.value;
  f.txtRfp_value.value=f.txtRfp.value;
  f.method = "POST";
  f.action = "/rfp_updaterecord/";
  f.submit();
}

function MainDelete()
{
  f = document.forms.frm;
  f.method ="POST";
  f.action="/rfp_deleterecord/";
  f.submit();
  
}

function MainReset()
{
 
  f = document.forms.frm;
  f.method ="POST";
  f.action="/rfp_kb/0";
  f.submit();
  
}

function MainNew()
{
  f = document.forms.frm;
  f.action = "/rfp_kb/0";
  f.method="POST";
  f.submit();
}