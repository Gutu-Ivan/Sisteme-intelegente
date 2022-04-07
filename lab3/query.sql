select name as author_name, year as publish_year, title as paper_title, pdf_name, abstract as paper_abstract, paper_text 
from authors a
join paper_authors pa on a.id = pa.author_id
join papers p on pa.paper_id = p.id
order by author_name