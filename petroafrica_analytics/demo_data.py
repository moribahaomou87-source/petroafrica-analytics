const form = document.getElementById('complianceForm');
const statusValue = document.getElementById('statusValue');
const reasonText = document.getElementById('reasonText');
const resultCard = document.getElementById('resultCard');
const metaList = document.getElementById('metaList');

function buildPayload(formData) {
  return {
    product_name: formData.get('product_name'),
    sample_code: formData.get('sample_code'),
    parameter: formData.get('parameter'),
    measured_value: formData.get('measured_value') ? Number(formData.get('measured_value')) : null,
    unit: formData.get('unit') || null,
    reference_conditions: formData.get('reference_conditions') || null,
    test_method: formData.get('test_method') || null,
    specification: {
      standard: formData.get('standard'),
      edition: formData.get('edition'),
      clause: formData.get('clause'),
      source_document: formData.get('source_document'),
      lower_limit: formData.get('lower_limit') ? Number(formData.get('lower_limit')) : null,
      upper_limit: formData.get('upper_limit') ? Number(formData.get('upper_limit')) : null,
      unit: formData.get('spec_unit') || null,
      reference_conditions: formData.get('spec_reference_conditions') || null,
      test_method: formData.get('spec_test_method') || null,
      type: 'product specification',
    },
  };
}

function updateDecision(result) {
  const normalized = result.status || 'indetermine';

  resultCard.className = `result-card ${normalized}`;
  statusValue.textContent = normalized;
  reasonText.textContent = result.reason || 'No reason available';

  metaList.innerHTML = `
    <li>Standard: ${result.standard || 'N/A'}</li>
    <li>Edition: ${result.edition || 'N/A'}</li>
    <li>Clause: ${result.clause || 'N/A'}</li>
    <li>Source: ${result.source_document || 'N/A'}</li>
  `;
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const payload = buildPayload(formData);

  try {
    const response = await fetch('/api/compliance/check', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    const result = await response.json();
    updateDecision(result);
  } catch (error) {
    statusValue.textContent = 'ERROR';
    reasonText.textContent = 'An unexpected error occurred during evaluation.';
    resultCard.className = 'result-card neutral';
  }
});
