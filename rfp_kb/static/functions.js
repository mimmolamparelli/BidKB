function Test()
{
  alert ('this is a test FUNCTION! ');
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
  // f = document.forms.frm;
  // question = f.elements.txtQuestion.value;
  alert ('Updating the current record:'+id);
}

function MainDelete()
{
  // f = document.forms.frm;
  // question = f.elements.txtQuestion.value;
  alert ('Deleting the current record');
}

function MainReset()
{
  window.location.href = "http://127.0.0.1:8000/rfp_kb/0";
}

