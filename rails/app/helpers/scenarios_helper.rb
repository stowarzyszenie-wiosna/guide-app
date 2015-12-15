module ScenariosHelper
  def step_type(index)
    case index.to_i
    when 1
      "Informacja"
    when 2
      "Pytanie"
    when 3
      "Interakcja"
    else
      "ERROR"
    end
  end
end
