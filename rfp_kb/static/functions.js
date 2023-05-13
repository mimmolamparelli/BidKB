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
  alert('main reset! 1')
  f = document.forms.frm;
  f.reset();
  
}

