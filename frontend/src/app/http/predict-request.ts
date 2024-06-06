export const API_URL = "http://localhost:5000";

export async function Predict(modelName: string, fruit: string, file: File) {
  const formData = new FormData();
  formData.append("model", modelName);
  formData.append("fruit", fruit);
  formData.append("file", file);

  const request = await fetch(`${API_URL}/predict`, {
    method: "POST",
    body: formData,
  });
  const response = await request.json();

  if (!request.ok) {
    throw new Error("Failed to predict");
  }

  return response;
}
