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
  alert('delete');
  f = document.forms.frm;
  f.elements.txtRfp.value="";
  f.elements.txtQuestion.value="";
  f.elements.txtAnswer.value="";
  f.elements.txtProduct.value="";
  f.elements.txtProductVariant.value="";
}

