function Test()
{
  alert ('this is a test FUNCTION! ');
  f = document.forms.frm;
  f.action = "/test/";
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

function MainAdd()
{
  f = document.forms.frm;
  // question = f.elements.txtQuestion.value;
  f.action = "/rfp_addrecord/";
  f.method="POST";
  f.submit();
  
}

function MainUpdate(id)
{
  
  f = document.forms.frm;
  alert ('Update !');
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