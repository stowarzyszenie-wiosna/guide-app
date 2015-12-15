json.array!(@steps) do |step|
  json.extract! step, :id, :message, :error_message, :options, :step_type, :group_id
  json.url step_url(step, format: :json)
end
